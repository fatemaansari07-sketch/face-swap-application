import cv2
import numpy as np


class ColorMatcher:

    def __init__(self):

        print("🎨 Color Matcher Loaded!")

    def analyze(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception("Image not found.")

        # Average BGR Color
        mean_bgr = np.mean(
            image,
            axis=(0, 1)
        )

        # Average HSV Color
        hsv = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2HSV
        )

        mean_hsv = np.mean(
            hsv,
            axis=(0, 1)
        )

        return {

            "blue": round(float(mean_bgr[0]), 2),
            "green": round(float(mean_bgr[1]), 2),
            "red": round(float(mean_bgr[2]), 2),

            "hue": round(float(mean_hsv[0]), 2),
            "saturation": round(float(mean_hsv[1]), 2),
            "value": round(float(mean_hsv[2]), 2),
        }

    def match(
        self,
        source_info,
        target_info,
    ):

        blue_diff = abs(
            source_info["blue"] -
            target_info["blue"]
        )

        green_diff = abs(
            source_info["green"] -
            target_info["green"]
        )

        red_diff = abs(
            source_info["red"] -
            target_info["red"]
        )

        hue_diff = abs(
            source_info["hue"] -
            target_info["hue"]
        )

        saturation_diff = abs(
            source_info["saturation"] -
            target_info["saturation"]
        )

        value_diff = abs(
            source_info["value"] -
            target_info["value"]
        )

        score = max(
            0,
            100 - (
                blue_diff * 0.15 +
                green_diff * 0.15 +
                red_diff * 0.15 +
                hue_diff * 0.20 +
                saturation_diff * 0.20 +
                value_diff * 0.15
            )
        )

        return {

            "score": round(score, 2),

            "blue_diff": round(blue_diff, 2),
            "green_diff": round(green_diff, 2),
            "red_diff": round(red_diff, 2),

            "hue_diff": round(hue_diff, 2),
            "saturation_diff": round(saturation_diff, 2),
            "value_diff": round(value_diff, 2),
        }