import cv2
from insightface.app import FaceAnalysis


class FaceObjects:

    def __init__(self):

        print("🧩 Face Objects Detector Loaded!")

        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640),
        )

    def analyze(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            return {
                "glasses": False,
                "beard": False,
                "score": 50,
            }

        faces = self.app.get(image)

        if not faces:
            return {
                "glasses": False,
                "beard": False,
                "score": 50,
            }

        face = faces[0]

        score = 100

        # Placeholder rules
        # Future me SAM + YOLO se actual detection hogi

        glasses = False
        beard = False

        if glasses:
            score -= 5

        if beard:
            score -= 3

        return {
            "glasses": glasses,
            "beard": beard,
            "score": score,
        }