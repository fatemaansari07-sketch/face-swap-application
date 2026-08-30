import cv2
from insightface.app import FaceAnalysis


class FaceDetector:

    def __init__(self):
        print("🧠 Loading Face Detection Model...")

        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(ctx_id=-1, det_size=(640, 640))

        print("✅ Face Detection Model Loaded!")

    def detect_faces(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise Exception(f"Image not found: {image_path}")

        faces = self.app.get(image)

        return image, faces