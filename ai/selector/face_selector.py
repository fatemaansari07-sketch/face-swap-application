import cv2


class FaceSelector:

    def __init__(self):

        print("🎯 Face Selector Loaded!")

    def select_best(self, image_paths, quality_engine):

        best_path = None
        best_score = -1

        scores = {}

        for image_path in image_paths:

            score = quality_engine.score(image_path)

            scores[image_path] = score

            print(
                f"⭐ {image_path} -> Quality: {score:.2f}"
            )

            if score > best_score:

                best_score = score
                best_path = image_path

        print(f"🏆 Best Face: {best_path}")

        return best_path, scores