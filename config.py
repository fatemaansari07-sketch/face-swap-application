import os
from dotenv import load_dotenv

load_dotenv()

# =====================================
# Telegram
# =====================================

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# =====================================
# App
# =====================================

APP_NAME = "AI Studio Engine"
APP_VERSION = "0.3.0"

# =====================================
# Folders
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")
MODEL_FOLDER = os.path.join(BASE_DIR, "models")

# =====================================
# Limits
# =====================================

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

# =====================================
# AI Models
# =====================================

INSWAPPER_MODEL = os.path.join(
    MODEL_FOLDER,
    "swapping",
    "inswapper_128.onnx",
)

SAM_MODEL = os.path.join(
    MODEL_FOLDER,
    "sam_vit_b.pth",
)