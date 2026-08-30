from ai.detection.face_detector import FaceDetector
from ai.identity.identity_engine import IdentityEngine
from ai.alignment.face_aligner import FaceAligner
from ai.occlusion.mask_generator import MaskGenerator
from ai.occlusion.occlusion_detector import OcclusionDetector
from ai.pose.face_pose import FacePose
from ai.swap.face_swapper import FaceSwapper
from ai.blending.face_blender import FaceBlender
from ai.enhancement.face_enhancer import FaceEnhancer
from ai.fusion.identity_fusion import IdentityFusion
from ai.quality.face_quality import FaceQuality
from ai.selector.face_selector import FaceSelector
from ai.objects.face_objects import FaceObjects
from ai.objects.face_attributes import FaceAttributes

from ai.lighting.light_matcher import LightMatcher
from ai.color.color_matcher import ColorMatcher
from ai.skin.skin_tone_matcher import SkinToneMatcher

from ai.matching.appearance_matcher import AppearanceMatcher


class AIPipeline:

    def __init__(self):

        print("🚀 Building AI Pipeline...")

        self.detector = FaceDetector()
        self.identity = IdentityEngine()
        self.aligner = FaceAligner()

        self.mask = MaskGenerator()
        self.occlusion = OcclusionDetector()
        self.pose = FacePose()

        self.swapper = FaceSwapper()
        self.blender = FaceBlender()
        self.enhancer = FaceEnhancer()

        self.fusion = IdentityFusion()
        self.quality = FaceQuality()
        self.selector = FaceSelector()

        self.objects = FaceObjects()
        self.attributes = FaceAttributes()

        # ------------------------------------------
        # Appearance Analysis
        # ------------------------------------------

        self.light_matcher = LightMatcher()
        self.color_matcher = ColorMatcher()
        self.skin_tone_matcher = SkinToneMatcher()

        # ------------------------------------------
        # Appearance Matching
        # ------------------------------------------

        self.appearance_matcher = AppearanceMatcher()

        print("🎨 Appearance Matching System Loaded!")

        print("✅ AI Pipeline Ready!")

    def process(
        self,
        source_path,
        target_path,
        output_path,
        left_path=None,
        center_path=None,
        right_path=None,
    ):

        print("\n========== AI STUDIO ENGINE ==========\n")

        # ==========================================
        # MULTI IDENTITY MODE
        # ==========================================

        if left_path and center_path and right_path:

            print("🧠 Multi Identity Mode\n")

            image_paths = [
                left_path,
                center_path,
                right_path,
            ]

            weights = []

            for path in image_paths:

                quality = self.quality.score(path)

                pose = self.pose.get_pose_score(path)

                occlusion = (
                    self.occlusion.get_occlusion_score(path)
                )

                objects = self.objects.analyze(path)

                attributes = self.attributes.analyze(path)

                score = (
                    quality["final_score"] * 0.30
                    + pose["score"] * 0.20
                    + occlusion["score"] * 0.20
                    + objects["score"] * 0.15
                    + attributes["score"] * 0.15
                )

                weights.append(score)

                print(f"\n📷 {path}")

                print(
                    f"⭐ Quality    : "
                    f"{quality['final_score']}"
                )

                print(
                    f"📐 Pose       : "
                    f"{pose['score']}"
                )

                print(
                    f"🙈 Occlusion  : "
                    f"{occlusion['score']}"
                )

                print(
                    f"🧩 Objects    : "
                    f"{objects['score']}"
                )

                print(
                    f"🎭 Attributes : "
                    f"{attributes['score']}"
                )

                print(
                    f"🏆 Weight     : "
                    f"{round(score, 2)}"
                )

            print("\n🧠 Creating Multi Identity...")

            fused_embedding = (
                self.identity.create_multi_identity(
                    image_paths=image_paths,
                    quality_scores=weights,
                )
            )

            print("🧠 Smart Identity Fusion...")

            fused_embedding = self.fusion.fuse(
                fused_embedding,
                fused_embedding,
                fused_embedding,
            )

            print(
                f"✅ Identity Vector Size : "
                f"{len(fused_embedding)}"
            )

            source_path = center_path

        # ==========================================
        # SINGLE MODE
        # ==========================================

        else:

            print("🙂 Single Identity Mode\n")

            quality = self.quality.score(
                source_path
            )

            pose = self.pose.get_pose_score(
                source_path
            )

            occlusion = (
                self.occlusion.get_occlusion_score(
                    source_path
                )
            )

            objects = self.objects.analyze(
                source_path
            )

            attributes = self.attributes.analyze(
                source_path
            )

            print(
                f"⭐ Quality    : "
                f"{quality['final_score']}"
            )

            print(
                f"📐 Pose       : "
                f"{pose['score']}"
            )

            print(
                f"🙈 Occlusion  : "
                f"{occlusion['score']}"
            )

            print(
                f"🧩 Objects    : "
                f"{objects['score']}"
            )

            print(
                f"🎭 Attributes : "
                f"{attributes['score']}"
            )

            embedding = self.identity.create_identity(
                source_path
            )

            fused_embedding = self.fusion.fuse(
                embedding,
                embedding,
                embedding,
            )

            print(
                f"✅ Identity Vector Size : "
                f"{len(fused_embedding)}"
            )

        # ==========================================
        # SOURCE / TARGET APPEARANCE ANALYSIS
        # ==========================================

        print(
            "\n🎨 Analyzing Source/Target Appearance..."
        )

        # ------------------------------------------
        # Lighting
        # ------------------------------------------

        print("\n💡 Lighting Analysis...")

        lighting_result = (
            self.light_matcher.match_images(
                source_path,
                target_path,
            )
        )

        print(
            f"💡 Lighting Score : "
            f"{lighting_result['score']}"
        )

        print(
            f"   Brightness Difference : "
            f"{lighting_result['brightness_difference']}"
        )

        print(
            f"   Contrast Difference   : "
            f"{lighting_result['contrast_difference']}"
        )

        # ------------------------------------------
        # Color
        # ------------------------------------------

        print("\n🎨 Color Analysis...")

        source_color = self.color_matcher.analyze(
            source_path
        )

        target_color = self.color_matcher.analyze(
            target_path
        )

        color_result = self.color_matcher.match(
            source_color,
            target_color,
        )

        print(
            f"🎨 Color Score : "
            f"{color_result['score']}"
        )

        # ------------------------------------------
        # Skin Tone
        # ------------------------------------------

        print("\n🧑 Skin Tone Analysis...")

        source_skin = self.skin_tone_matcher.analyze(
            source_path
        )

        target_skin = self.skin_tone_matcher.analyze(
            target_path
        )

        skin_result = self.skin_tone_matcher.match(
            source_skin,
            target_skin,
        )

        print(
            f"🧑 Skin Tone Score : "
            f"{skin_result['score']}"
        )

        # ==========================================
        # APPEARANCE COMPATIBILITY
        # ==========================================

        print(
            "\n🎯 Calculating Appearance Compatibility..."
        )

        appearance_result = (
            self.appearance_matcher.calculate(
                lighting_score=lighting_result["score"],
                color_score=color_result["score"],
                skin_score=skin_result["score"],
            )
        )

        print(
            f"💡 Lighting : "
            f"{appearance_result['lighting']}"
        )

        print(
            f"🎨 Color    : "
            f"{appearance_result['color']}"
        )

        print(
            f"🧑 Skin     : "
            f"{appearance_result['skin']}"
        )

        print(
            f"🏆 Appearance Score : "
            f"{appearance_result['final_score']}"
        )

        # ==========================================
        # ALIGNMENT
        # ==========================================

        print("\n📐 Aligning Face...")

        # Future integration

        # ==========================================
        # MASK
        # ==========================================

        print("🎭 Creating Face Mask...")

        # Future integration

        # ==========================================
        # FACE SWAP
        # ==========================================

        print("🔄 Swapping Face...")

        self.swapper.swap(
            source_path=source_path,
            target_path=target_path,
            output_path=output_path,
            fused_embedding=fused_embedding,
        )

        # ==========================================
        # BLENDING
        # ==========================================

        print("🎨 Blending Face...")

        # Future integration

        # ==========================================
        # ENHANCEMENT
        # ==========================================

        print("✨ Enhancing Face...")

        # Future integration

        # ==========================================
        # FINAL SUMMARY
        # ==========================================

        print(
            "\n📊 Appearance Compatibility Summary"
        )

        print(
            f"💡 Lighting : "
            f"{appearance_result['lighting']}"
        )

        print(
            f"🎨 Color    : "
            f"{appearance_result['color']}"
        )

        print(
            f"🧑 Skin     : "
            f"{appearance_result['skin']}"
        )

        print(
            f"🏆 Appearance : "
            f"{appearance_result['final_score']}"
        )

        print(
            "\n🎉 AI Studio Engine Finished!\n"
        )

        return output_path