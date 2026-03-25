import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

from app.bot.handlers import handle_ask, handle_help, handle_summarize

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("ask", handle_ask))
    app.add_handler(CommandHandler("help", handle_help))
    app.add_handler(CommandHandler("summarize", handle_summarize))

    print("Bot is running...")
    app.run_polling()