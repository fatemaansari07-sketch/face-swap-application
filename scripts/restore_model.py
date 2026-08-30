"""Reassemble and verify the InSwapper model committed in repository parts."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


MODEL_DIR = Path(__file__).resolve().parents[1] / "models" / "swapping"
MODEL_PATH = MODEL_DIR / "inswapper_128.onnx"
PART_PATTERN = "inswapper_128.onnx.part-*"
EXPECTED_SIZE = 554_253_681
EXPECTED_SHA256 = (
    "e4a3f08c753cb72d04e10aa0f7dbe3deebbf39567d4ead6dce08e98aa49e16af"
)


def checksum(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as model:
        for block in iter(lambda: model.read(1024 * 1024), b""):
            size += len(block)
            digest.update(block)
    return size, digest.hexdigest()


def restore() -> None:
    if MODEL_PATH.exists():
        size, digest = checksum(MODEL_PATH)
        if size == EXPECTED_SIZE and digest == EXPECTED_SHA256:
            print(f"Model already restored: {MODEL_PATH}")
            return
        raise RuntimeError(
            f"Existing model failed verification: {MODEL_PATH}. "
            "Remove it and run this script again."
        )

    parts = sorted(MODEL_DIR.glob(PART_PATTERN))
    if not parts:
        raise FileNotFoundError(
            f"No model parts found in {MODEL_DIR}. "
            "Clone the complete repository before restoring the model."
        )

    temporary_path = MODEL_PATH.with_suffix(".onnx.tmp")
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    with temporary_path.open("wb") as restored:
        for part in parts:
            print(f"Appending {part.name}")
            with part.open("rb") as source:
                for block in iter(lambda: source.read(1024 * 1024), b""):
                    restored.write(block)
    os.replace(temporary_path, MODEL_PATH)

    size, digest = checksum(MODEL_PATH)
    if size != EXPECTED_SIZE or digest != EXPECTED_SHA256:
        MODEL_PATH.unlink(missing_ok=True)
        raise RuntimeError("Restored model failed size or SHA-256 verification.")

    print(f"Model restored and verified: {MODEL_PATH}")


if __name__ == "__main__":
    restore()