import os
import logging
import asyncio
from flask import Flask, send_file
from telegram import Update, WebAppInfo, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL", "")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

web = Flask(__name__)

@web.route("/")
def index():
    return send_file(os.path.join(os.path.dirname(__file__), "index.html"))

@web.route("/health")
def health():
    return "ok", 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = APP_URL if APP_URL else f"https://{os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost')}"
    await update.message.reply_text(
        "👋 Привіт! Натисни кнопку нижче, щоб відкрити ОБЛІК.",
        reply_markup={
            "inline_keyboard": [[{
                "text": "📊 Відкрити ОБЛІК",
                "web_app": {"url": url}
            }]]
        }
    )

async def post_init(application):
    url = APP_URL if APP_URL else f"https://{os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost')}"
    try:
        await application.bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(
                text="ОБЛІК",
                web_app=WebAppInfo(url=url)
            )
        )
        logger.info(f"Menu button set to {url}")
    except Exception as e:
        logger.warning(f"Could not set menu button: {e}")

async def run_bot_async():
    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("Bot starting...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    logger.info("Bot is running")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(run_bot_async())
