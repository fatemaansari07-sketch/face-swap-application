import cv2

from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model

from config import INSWAPPER_MODEL

from ai.matching.identity_matcher import IdentityMatcher


class FaceSwapper:

    def __init__(self):

        print("🚀 Loading Face Swap Model...")

        # ==================================
        # FACE ANALYSIS
        # ==================================

        self.app = FaceAnalysis(
            name="buffalo_l"
        )

        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640),
        )

        # ==================================
        # INSWAPPER MODEL
        # ==================================

        self.swapper = get_model(
            INSWAPPER_MODEL
        )

        # ==================================
        # IDENTITY MATCHER
        # ==================================

        self.matcher = IdentityMatcher()

        print(
            "✅ Face Swap Model Loaded!"
        )

    def swap(
        self,
        source_path,
        target_path,
        output_path,
        fused_embedding=None,
    ):

        print(
            "\n========== RAW FACE SWAP ==========\n"
        )

        # ==================================
        # READ IMAGES
        # ==================================

        print("📖 Reading Images...")

        source = cv2.imread(
            source_path
        )

        target = cv2.imread(
            target_path
        )

        if source is None:

            raise Exception(
                "Source image not found."
            )

        if target is None:

            raise Exception(
                "Target image not found."
            )

        # ==================================
        # FACE DETECTION
        # ==================================

        print("🙂 Detecting Faces...")

        source_faces = self.app.get(
            source
        )

        target_faces = self.app.get(
            target
        )

        if not source_faces:

            raise Exception(
                "No face found in Source Image."
            )

        if not target_faces:

            raise Exception(
                "No face found in Target Image."
            )

        print(
            f"👤 Source Faces : "
            f"{len(source_faces)}"
        )

        print(
            f"👥 Target Faces : "
            f"{len(target_faces)}"
        )

        # ==================================
        # SOURCE FACE
        # ==================================

        source_face = source_faces[0]

        # ==================================
        # TARGET FACE SELECTION
        # ==================================

        if (
            fused_embedding is not None
            and len(target_faces) > 1
        ):

            print(
                "\n🎯 Searching Best Matching Face..."
            )

            target_face, score = (
                self.matcher.find_best_match(
                    fused_embedding,
                    source_face,
                    target_faces,
                )
            )

            print(
                f"🏆 Final Match Score : "
                f"{round(score, 2)}"
            )

        else:

            target_face = target_faces[0]

            print(
                "🙂 Single Target Face Selected."
            )

        # ==================================
        # RAW FACE SWAP
        # ==================================

        print(
            "\n🔄 Performing RAW InSwapper..."
        )

        result = self.swapper.get(
            target,
            target_face,
            source_face,
            paste_back=True,
        )

        if result is None:

            raise Exception(
                "Face swap returned empty result."
            )

        print(
            "✅ RAW InSwapper Result Created!"
        )

        # ==================================
        # SAVE RAW RESULT
        # ==================================

        print(
            "💾 Saving RAW Swap Result..."
        )

        success = cv2.imwrite(
            output_path,
            result,
        )

        if not success:

            raise Exception(
                "Failed to save output image."
            )

        # ==================================
        # FINISHED
        # ==================================

        print(
            "\n🎉 RAW Face Swap Finished!"
        )

        print(
            f"📁 Output : {output_path}"
        )

        return output_path