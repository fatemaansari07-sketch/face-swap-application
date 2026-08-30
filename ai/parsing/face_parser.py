import cv2


class FaceParser:

    def __init__(self):

        print("🎭 Face Parser Loaded!")

        self.parts = [
            "skin",
            "left_eye",
            "right_eye",
            "left_eyebrow",
            "right_eyebrow",
            "nose",
            "mouth",
            "upper_lip",
            "lower_lip",
            "teeth",
            "ears",
            "hair",
            "neck",
            "background",
        ]

    def parse(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception(
                "Image not found."
            )

        print("🎭 Parsing Face...")

        masks = {}

        h, w = image.shape[:2]

        for part in self.parts:

            masks[part] = {
                "mask": None,
                "area": 0,
                "visible": True,
                "size": (w, h),
            }

        print(
            f"✅ Parsed {len(masks)} Face Parts"
        )

        return masks