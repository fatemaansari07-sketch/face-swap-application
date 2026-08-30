import cv2
import numpy as np
from insightface.app import FaceAnalysis


class IdentityEngine:

    def __init__(self):

        print("🧠 Loading Identity Engine...")

        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(ctx_id=-1, det_size=(640, 640))

        print("✅ Identity Engine Ready!")

    def create_identity(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception("Image not found.")

        faces = self.app.get(image)

        if len(faces) == 0:
            raise Exception("No face found.")

        return faces[0].embedding

    def create_multi_identity(
        self,
        image_paths,
        quality_scores=None,
    ):

        embeddings = []
        weights = []

        for i, image_path in enumerate(image_paths):

            try:

                embedding = self.create_identity(image_path)

                embeddings.append(embedding)

                if quality_scores is None:
                    weights.append(1.0)
                else:
                    weights.append(
                        quality_scores[i]
                    )

            except Exception as e:

                print(e)

        if len(embeddings) == 0:
            raise Exception(
                "No valid identity images found."
            )

        weights = np.array(weights)

        weights = weights / weights.sum()

        fused = np.average(
            embeddings,
            axis=0,
            weights=weights,
        )

        return fused

    def process(
        self,
        source_faces,
        target_faces,
    ):

        return True