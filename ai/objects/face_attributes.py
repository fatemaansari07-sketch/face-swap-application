import cv2
from insightface.app import FaceAnalysis


class FaceAttributes:

    def __init__(self):

        print("🧩 Face Attributes Loaded!")

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
                "mustache": False,
                "mask": False,
                "hat": False,
                "eyes_visible": False,
                "mouth_visible": False,
                "hair_visible": False,
                "score": 0,
            }

        faces = self.app.get(image)

        if not faces:

            return {
                "glasses": False,
                "beard": False,
                "mustache": False,
                "mask": False,
                "hat": False,
                "eyes_visible": False,
                "mouth_visible": False,
                "hair_visible": False,
                "score": 0,
            }

        face = faces[0]

        yaw, pitch, roll = face.pose

        score = 100

        if abs(yaw) > 35:
            score -= 20

        if abs(pitch) > 25:
            score -= 15

        if abs(roll) > 25:
            score -= 10

        return {

            # Future AI Detection
            "glasses": False,
            "beard": False,
            "mustache": False,
            "mask": False,
            "hat": False,

            # Estimated visibility
            "eyes_visible": abs(yaw) < 40,
            "mouth_visible": abs(pitch) < 35,
            "hair_visible": True,

            "score": max(0, score),
        }