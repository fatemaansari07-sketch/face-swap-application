# AI Studio Engine

AI Studio Engine is a Telegram bot for multi-angle identity face swapping. The
current implementation accepts left, front, and right reference photos, then a
target image, and returns a face-swapped result.

## What is included

- Telegram bot handlers and four-step photo workflow
- Multi-angle identity embedding and quality scoring
- Face detection, alignment, occlusion, appearance, color, lighting, and
  blending modules
- InSwapper face-swap pipeline using CPU inference
- Flask health endpoint for local or hosted process checks
- Complete InSwapper model stored as sub-100 MB repository parts, with a
  checksum-verified restore script

Video face swap, profile, credits, and settings are currently marked as
under development in the bot menu.

## Requirements

- Python 3.11 or newer
- A Telegram bot token from BotFather
- Enough disk space for the InSwapper model and InsightFace's first-run model
  download

## Setup

```bash
git clone <repository-url>
cd face-swap-application

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

cp .env.example .env
python scripts/restore_model.py
```

Edit `.env` and set:

```dotenv
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=0
```

The `.env` file is intentionally ignored by Git. Never commit tokens or other
credentials.

## Run the bot

```bash
python main.py
```

On its first run, InsightFace downloads the `buffalo_l` analysis model to the
user model cache. The restore script combines the committed model parts into
`models/swapping/inswapper_128.onnx` and verifies its size and SHA-256 checksum.

## Run the health endpoint

The small Flask endpoint is useful for a process or platform health check:

```bash
python app.py
```

It listens on `http://127.0.0.1:8080/` and responds with a running message.
The health endpoint does not start the Telegram bot.

## Project layout

```text
ai/                 Face analysis and swap pipeline modules
bot/                Telegram handlers
database/           In-memory user session state
models/swapping/    Committed model parts and restored model location
scripts/            Model restore utility
app.py              Flask health endpoint
config.py           Environment-backed configuration
main.py             Telegram bot entry point
requirements.txt    Python dependencies
```

## Notes

- This project uses CPU inference (`ctx_id=-1`); GPU execution is not required.
- Uploaded images, generated outputs, local caches, Python bytecode, the
  assembled model, and archives are excluded from the repository.
- Use face images only with the appropriate consent and rights.