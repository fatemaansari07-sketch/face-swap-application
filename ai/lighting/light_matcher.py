import cv2
import numpy as np


class LightMatcher:

    def __init__(self):

        print("💡 Light Matcher Loaded!")

    def analyze(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception(
                f"Image not found: {image_path}"
            )

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        brightness = float(
            np.mean(gray)
        )

        contrast = float(
            np.std(gray)
        )

        return {
            "brightness": round(brightness, 2),
            "contrast": round(contrast, 2),
        }

    def match(
        self,
        source_info,
        target_info,
    ):

        print("💡 Matching Lighting...")

        brightness_diff = abs(
            source_info["brightness"]
            - target_info["brightness"]
        )

        contrast_diff = abs(
            source_info["contrast"]
            - target_info["contrast"]
        )

        score = max(
            0,
            100 - (
                brightness_diff * 0.5
                + contrast_diff * 0.5
            )
        )

        return {
            "score": round(score, 2),
            "brightness_difference": round(
                brightness_diff, 2
            ),
            "contrast_difference": round(
                contrast_diff, 2
            ),
        }

    def match_images(
        self,
        source_path,
        target_path,
    ):

        source_info = self.analyze(
            source_path
        )

        target_info = self.analyze(
            target_path
        )

        return self.match(
            source_info,
            target_info,
        )