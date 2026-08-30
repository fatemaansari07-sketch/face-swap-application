import os
import cv2
import numpy as np

try:
    import torch
    from segment_anything import sam_model_registry
    from segment_anything import SamPredictor

    SAM_AVAILABLE = True

except Exception:

    SAM_AVAILABLE = False


class MaskGenerator:

    def __init__(
        self,
        model_path="models/sam_vit_b.pth",
    ):

        print("🎭 Loading Mask Generator...")

        if not SAM_AVAILABLE:

            print("⚠️ SAM libraries not installed.")
            self.predictor = None
            return

        if not os.path.exists(model_path):

            print(f"⚠️ SAM model not found: {model_path}")
            self.predictor = None
            return

        device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        sam = sam_model_registry["vit_b"](
            checkpoint=model_path
        )

        sam.to(device)

        self.predictor = SamPredictor(sam)

        print(
            f"✅ Mask Generator Ready ({device.upper()})"
        )

    def generate_mask(
        self,
        image_path,
        box,
    ):

        if self.predictor is None:

            print("⚠️ SAM disabled. Skipping mask generation.")
            return None

        image = cv2.imread(image_path)

        if image is None:
            raise Exception("Image not found.")

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB,
        )

        self.predictor.set_image(image)

        masks, scores, logits = self.predictor.predict(
            box=np.array(box),
            multimask_output=False,
        )

        return masks[0]