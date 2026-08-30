import numpy as np


class IdentityMatcher:

    def __init__(self):

        print("🎯 Identity Matcher Loaded!")

    # ------------------------------------

    def cosine_similarity(
        self,
        emb1,
        emb2,
    ):

        emb1 = emb1 / np.linalg.norm(emb1)
        emb2 = emb2 / np.linalg.norm(emb2)

        return float(
            np.dot(emb1, emb2)
        )

    # ------------------------------------

    def pose_score(
        self,
        source_face,
        target_face,
    ):

        try:

            sy, sp, sr = source_face.pose
            ty, tp, tr = target_face.pose

            diff = (
                abs(sy - ty)
                + abs(sp - tp)
                + abs(sr - tr)
            )

            score = max(
                0,
                100 - diff,
            )

            return score

        except:

            return 50

    # ------------------------------------

    def size_score(
        self,
        source_face,
        target_face,
    ):

        try:

            sx1, sy1, sx2, sy2 = source_face.bbox
            tx1, ty1, tx2, ty2 = target_face.bbox

            s_area = (
                (sx2 - sx1)
                * (sy2 - sy1)
            )

            t_area = (
                (tx2 - tx1)
                * (ty2 - ty1)
            )

            ratio = min(
                s_area,
                t_area,
            ) / max(
                s_area,
                t_area,
            )

            return ratio * 100

        except:

            return 50

    # ------------------------------------

    def position_score(
        self,
        source_face,
        target_face,
    ):

        try:

            sx1, sy1, sx2, sy2 = source_face.bbox
            tx1, ty1, tx2, ty2 = target_face.bbox

            scx = (sx1 + sx2) / 2
            scy = (sy1 + sy2) / 2

            tcx = (tx1 + tx2) / 2
            tcy = (ty1 + ty2) / 2

            dist = np.sqrt(
                (scx - tcx) ** 2
                + (scy - tcy) ** 2
            )

            score = max(
                0,
                100 - (dist / 5),
            )

            return score

        except:

            return 50

    # ------------------------------------

    def find_best_match(
        self,
        fused_embedding,
        source_face,
        target_faces,
    ):

        best_face = None
        best_score = -1

        for face in target_faces:

            identity = (
                self.cosine_similarity(
                    fused_embedding,
                    face.embedding,
                )
                * 100
            )

            pose = self.pose_score(
                source_face,
                face,
            )

            size = self.size_score(
                source_face,
                face,
            )

            position = self.position_score(
                source_face,
                face,
            )

            final_score = (
                identity * 0.50
                + pose * 0.20
                + size * 0.15
                + position * 0.15
            )

            print("\n========================")
            print(
                f"🎯 Identity : {round(identity,2)}"
            )
            print(
                f"📐 Pose     : {round(pose,2)}"
            )
            print(
                f"📦 Size     : {round(size,2)}"
            )
            print(
                f"📍 Position : {round(position,2)}"
            )
            print(
                f"🏆 Final    : {round(final_score,2)}"
            )

            if final_score > best_score:

                best_score = final_score
                best_face = face

        print("\n========================")
        print(
            f"🥇 Best Match : {round(best_score,2)}"
        )

        return best_face, best_score