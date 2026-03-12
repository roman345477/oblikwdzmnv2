import os
import logging
import asyncio
from flask import Flask, send_file
from telegram import Update, WebAppInfo, MenuButtonWebApp, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ─── Config ───
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
RAILWAY_DOMAIN = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "")
APP_URL = os.environ.get("APP_URL", "")

def get_url():
    if APP_URL:
        return APP_URL
    if RAILWAY_DOMAIN:
        return f"https://{RAILWAY_DOMAIN}"
    return "https://localhost"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# ─── Flask (для gunicorn) ───
web = Flask(__name__)

@web.route("/")
def index():
    return send_file(os.path.join(os.path.dirname(__file__), "index.html"))

@web.route("/health")
def health():
    return "ok", 200

# ─── Telegram Bot ───
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_url()
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Відкрити ОБЛІК", web_app=WebAppInfo(url=url))]
    ])
    await update.message.reply_text(
        "👋 Натисни кнопку, щоб відкрити трекер годин:",
        reply_markup=keyboard
    )

async def post_init(application):
    url = get_url()
    try:
        await application.bot.set_chat_menu_button(
            menu_button=MenuButtonWebApp(text="ОБЛІК", web_app=WebAppInfo(url=url))
        )
        logger.info(f"Menu button → {url}")
    except Exception as e:
        logger.warning(f"Menu button error: {e}")

async def run_bot_async():
    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("🤖 Bot polling...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    logger.info("Bot is running")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set!")
    else:
        asyncio.run(run_bot_async())
