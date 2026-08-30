import numpy as np


class IdentityFusion:

    def __init__(self):

        print("🧠 Identity Fusion Loaded!")

    def fuse(
        self,
        left_embedding,
        center_embedding,
        right_embedding,
        left_weight=1.0,
        center_weight=1.0,
        right_weight=1.0,
    ):

        embeddings = np.array([
            left_embedding,
            center_embedding,
            right_embedding,
        ])

        weights = np.array([
            left_weight,
            center_weight,
            right_weight,
        ])

        weights = weights / weights.sum()

        fused = np.average(
            embeddings,
            axis=0,
            weights=weights,
        )

        return fused