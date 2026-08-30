import os

from telegram import Update
from telegram.ext import ContextTypes

from ai.manager import AIManager
from database.session_manager import session

manager = AIManager()


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not session.exists(user_id):
        return

    state = session.get_state(user_id)

    photo = update.message.photo[-1]

    user_folder = f"uploads/{user_id}"
    os.makedirs(user_folder, exist_ok=True)

    photo_file = await photo.get_file()

    # ---------------- LEFT ----------------

    if state == "waiting_left":

        path = f"{user_folder}/left.jpg"

        await photo_file.download_to_drive(path)

        session.set_image(user_id, "left", path)
        session.set_state(user_id, "waiting_center")

        await update.message.reply_text(
            "✅ LEFT Face Saved.\n\n"
            "📸 Step 2/4\n"
            "🙂 Now send your FRONT Face."
        )

        return

    # ---------------- CENTER ----------------

    elif state == "waiting_center":

        path = f"{user_folder}/center.jpg"

        await photo_file.download_to_drive(path)

        session.set_image(user_id, "center", path)
        session.set_state(user_id, "waiting_right")

        await update.message.reply_text(
            "✅ FRONT Face Saved.\n\n"
            "📸 Step 3/4\n"
            "➡️ Now send your RIGHT Face."
        )

        return

    # ---------------- RIGHT ----------------

    elif state == "waiting_right":

        path = f"{user_folder}/right.jpg"

        await photo_file.download_to_drive(path)

        session.set_image(user_id, "right", path)
        session.set_state(user_id, "waiting_target")

        await update.message.reply_text(
            "✅ RIGHT Face Saved.\n\n"
            "📸 Step 4/4\n"
            "🖼 Now send your TARGET Image."
        )

        return

    # ---------------- TARGET ----------------

    elif state == "waiting_target":

        target_path = f"{user_folder}/target.jpg"

        await photo_file.download_to_drive(target_path)

        session.set_image(user_id, "target", target_path)

        progress = await update.message.reply_text(
            "🧠 Building Multi Identity...\n"
            "⏳ Please wait..."
        )

        output_path = f"{user_folder}/result.jpg"

        try:

            await progress.edit_text(
                "🔍 Analyzing Faces...\n"
                "⏳ Please wait..."
            )

            manager.face_swap(
                left_path=session.get_image(user_id, "left"),
                center_path=session.get_image(user_id, "center"),
                right_path=session.get_image(user_id, "right"),
                target_path=session.get_image(user_id, "target"),
                output_path=output_path,
            )

            await progress.edit_text(
                "📤 Uploading Result..."
            )

            with open(output_path, "rb") as photo:

                await update.message.reply_photo(
                    photo=photo,
                    caption="✅ Face Swap Completed!"
                )

            with open(output_path, "rb") as document:

                await update.message.reply_document(
                    document=document,
                    filename="AI_Studio_FaceSwap.jpg",
                    caption="📥 Original Quality Download"
                )

            await progress.delete()

        except Exception as e:

            await progress.edit_text(
                f"❌ Error:\n{e}"
            )

        session.clear(user_id)