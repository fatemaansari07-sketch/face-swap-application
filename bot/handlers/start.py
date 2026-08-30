from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import ContextTypes

from config import (
    APP_NAME,
    APP_VERSION,
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    keyboard = [
        ["🖼 Face Swap", "🎥 Video Face Swap"],
        ["👤 My Profile", "💎 Credits"],
        ["⚙ Settings", "ℹ Help"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False,
    )

    message = (
        f"👋 Welcome to {APP_NAME}\n\n"
        f"🚀 Version: {APP_VERSION}\n\n"
        "Choose an option below."
    )

    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
    )