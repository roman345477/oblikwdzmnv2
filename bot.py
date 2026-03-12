import os
import logging
from threading import Thread
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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ─── Flask: serve the HTML ───
web = Flask(__name__)

@web.route("/")
def index():
    return send_file("index.html")

@web.route("/health")
def health():
    return "ok", 200

def run_web():
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Flask starting on port {port}")
    web.run(host="0.0.0.0", port=port, debug=False)

# ─── Telegram Bot ───
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = get_url()
    logger.info(f"/start from {update.effective_user.id}, url={url}")
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
            menu_button=MenuButtonWebApp(
                text="ОБЛІК",
                web_app=WebAppInfo(url=url)
            )
        )
        logger.info(f"Menu button → {url}")
    except Exception as e:
        logger.warning(f"Menu button error: {e}")

def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN not set! Add it in Railway Variables.")
        return

    logger.info(f"URL: {get_url()}")

    # Flask in background
    t = Thread(target=run_web, daemon=True)
    t.start()

    # Telegram bot
    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("🤖 Bot polling...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
