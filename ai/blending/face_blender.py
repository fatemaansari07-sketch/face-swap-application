import cv2
import numpy as np


class FaceBlender:

    def __init__(self):

        print("🎨 Face Blender Loaded!")

    def create_face_mask(
        self,
        image_shape,
        face,
    ):

        height, width = image_shape[:2]

        mask = np.zeros(
            (height, width),
            dtype=np.uint8,
        )

        # ------------------------------------------
        # Try detailed 106-point landmarks
        # ------------------------------------------

        landmarks = getattr(
            face,
            "landmark_2d_106",
            None,
        )

        if landmarks is not None:

            points = np.asarray(
                landmarks,
                dtype=np.int32,
            )

            if len(points) >= 20:

                hull = cv2.convexHull(
                    points
                )

                cv2.fillConvexPoly(
                    mask,
                    hull,
                    255,
                )

        # ------------------------------------------
        # Fallback: face bounding box
        # ------------------------------------------

        else:

            bbox = face.bbox.astype(int)

            x1, y1, x2, y2 = bbox

            cv2.ellipse(
                mask,
                (
                    int((x1 + x2) / 2),
                    int((y1 + y2) / 2),
                ),
                (
                    int((x2 - x1) * 0.50),
                    int((y2 - y1) * 0.58),
                ),
                0,
                0,
                360,
                255,
                -1,
            )

        # ------------------------------------------
        # Expand slightly
        # ------------------------------------------

        kernel = np.ones(
            (9, 9),
            np.uint8,
        )

        mask = cv2.dilate(
            mask,
            kernel,
            iterations=1,
        )

        # ------------------------------------------
        # Feather edge
        # ------------------------------------------

        mask = cv2.GaussianBlur(
            mask,
            (31, 31),
            0,
        )

        return mask

    # ------------------------------------------
    # Main blending
    # ------------------------------------------

    def blend(
        self,
        original_image,
        swapped_image,
        face,
    ):

        print("🎨 Creating Face Blend Mask...")

        if original_image is None:
            raise ValueError(
                "Original image is None."
            )

        if swapped_image is None:
            raise ValueError(
                "Swapped image is None."
            )

        if original_image.shape != swapped_image.shape:

            swapped_image = cv2.resize(
                swapped_image,
                (
                    original_image.shape[1],
                    original_image.shape[0],
                ),
            )

        mask = self.create_face_mask(
            original_image.shape,
            face,
        )

        # ------------------------------------------
        # Convert mask to alpha
        # ------------------------------------------

        alpha = (
            mask.astype(np.float32)
            / 255.0
        )

        alpha = alpha[..., np.newaxis]

        # ------------------------------------------
        # Blend
        # ------------------------------------------

        result = (
            swapped_image.astype(
                np.float32
            )
            * alpha
            +
            original_image.astype(
                np.float32
            )
            * (1.0 - alpha)
        )

        result = np.clip(
            result,
            0,
            255,
        ).astype(np.uint8)

        print(
            "✅ Face edges softened and blended!"
        )

        return result