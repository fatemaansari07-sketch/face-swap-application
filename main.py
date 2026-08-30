from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import (
    BOT_TOKEN,
    APP_NAME,
    APP_VERSION,
)

from bot.handlers.start import start
from bot.handlers.menu import menu_handler
from bot.handlers.photo import photo_handler


def main():

    print("=" * 45)
    print(f"🚀 {APP_NAME}")
    print(f"📦 Version : {APP_VERSION}")
    print("=" * 45)

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # Menu
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu_handler
        )
    )

    # Photos
    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            photo_handler
        )
    )

    print("🤖 AI Studio Engine Started Successfully!")
    print("⏳ Waiting for users...\n")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()