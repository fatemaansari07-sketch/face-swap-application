import cv2
import numpy as np


class SkinToneMatcher:

    def __init__(self):

        print("🧑 Skin Tone Matcher Loaded!")

    def analyze(
        self,
        image_path,
    ):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception("Image not found.")

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2LAB,
        )

        mean_lab = np.mean(
            image,
            axis=(0, 1),
        )

        return {

            "l": round(float(mean_lab[0]), 2),
            "a": round(float(mean_lab[1]), 2),
            "b": round(float(mean_lab[2]), 2),
        }

    def match(
        self,
        source_info,
        target_info,
    ):

        l_diff = abs(
            source_info["l"] -
            target_info["l"]
        )

        a_diff = abs(
            source_info["a"] -
            target_info["a"]
        )

        b_diff = abs(
            source_info["b"] -
            target_info["b"]
        )

        score = max(
            0,
            100 - (
                l_diff * 0.4 +
                a_diff * 0.3 +
                b_diff * 0.3
            )
        )

        return {

            "score": round(score, 2),

            "light_diff": round(l_diff, 2),

            "green_red_diff": round(a_diff, 2),

            "blue_yellow_diff": round(b_diff, 2),
        }