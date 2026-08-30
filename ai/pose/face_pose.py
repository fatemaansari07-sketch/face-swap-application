import cv2
from insightface.app import FaceAnalysis


class FacePose:

    def __init__(self):

        print("📐 Face Pose Estimator Loaded!")

        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640),
        )

    def estimate(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            return {
                "yaw": 0,
                "pitch": 0,
                "roll": 0,
            }

        faces = self.app.get(image)

        if not faces:
            return {
                "yaw": 0,
                "pitch": 0,
                "roll": 0,
            }

        yaw, pitch, roll = faces[0].pose

        return {
            "yaw": round(float(yaw), 2),
            "pitch": round(float(pitch), 2),
            "roll": round(float(roll), 2),
        }

    def get_pose_score(self, image_path):

        pose = self.estimate(image_path)

        yaw = abs(pose["yaw"])
        pitch = abs(pose["pitch"])
        roll = abs(pose["roll"])

        score = 100

        score -= yaw * 0.8
        score -= pitch * 0.5
        score -= roll * 0.3

        score = max(0, min(100, score))

        return {
            "score": round(score, 2),
            "pose": pose,
        }