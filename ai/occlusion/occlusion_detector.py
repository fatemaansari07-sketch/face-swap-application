import cv2
from insightface.app import FaceAnalysis


class OcclusionDetector:

    def __init__(self):

        print("🙈 Occlusion Detector Loaded!")

        self.app = FaceAnalysis(name="buffalo_l")
        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640),
        )

    def analyze(self, image_path):

        image = cv2.imread(image_path)

        if image is None:

            return {
                "occlusion": 100,
                "visible": False,
            }

        faces = self.app.get(image)

        if not faces:

            return {
                "occlusion": 100,
                "visible": False,
            }

        face = faces[0]

        x1, y1, x2, y2 = map(
            int,
            face.bbox,
        )

        face_area = max(
            1,
            (x2 - x1) * (y2 - y1),
        )

        image_area = (
            image.shape[0]
            * image.shape[1]
        )

        visibility = (
            face_area / image_area
        ) * 100

        occlusion = max(
            0,
            100 - visibility,
        )

        return {
            "occlusion": round(occlusion, 2),
            "visible": True,
        }

    def get_occlusion_score(self, image_path):

        result = self.analyze(image_path)

        score = max(
            0,
            100 - result["occlusion"],
        )

        return {
            "score": round(score, 2),
            "details": result,
        }