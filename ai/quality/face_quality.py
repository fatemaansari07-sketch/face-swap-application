import cv2
import numpy as np


class FaceQuality:

    def __init__(self):

        print("⭐ Face Quality Analyzer Loaded!")

    def score(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            return {
                "resolution": 0,
                "blur": 0,
                "brightness": 0,
                "final_score": 0,
            }

        # Resolution
        h, w = image.shape[:2]
        resolution = (w * h) / 100000

        # Blur Score
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blur = cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

        blur = min(blur / 100, 10)

        # Brightness
        brightness = np.mean(gray)

        brightness = brightness / 25.5

        # Final Score
        final_score = (
            resolution * 0.35 +
            blur * 0.40 +
            brightness * 0.25
        )

        return {
            "resolution": round(resolution, 2),
            "blur": round(blur, 2),
            "brightness": round(brightness, 2),
            "final_score": round(final_score, 2),
        }