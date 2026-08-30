from telegram import Update
from telegram.ext import ContextTypes

from database.session_manager import session


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id

    if text == "🖼 Face Swap":

        session.create_user(user_id)

        await update.message.reply_text(
            "⬅️ Step 1/4\n\n"
            "📷 Please send your LEFT Face.\n\n"
            "👉 Turn your face towards LEFT side."
        )

    elif text == "🎥 Video Face Swap":

        await update.message.reply_text(
            "🎬 Video Face Swap is under development."
        )

    elif text == "👤 My Profile":

        await update.message.reply_text(
            "👤 Profile system is under development."
        )

    elif text == "💎 Credits":

        await update.message.reply_text(
            "💎 Credits system is under development."
        )

    elif text == "⚙ Settings":

        await update.message.reply_text(
            "⚙ Settings are coming soon."
        )

    elif text == "ℹ Help":

        await update.message.reply_text(
            "ℹ Help section is under development."
        )