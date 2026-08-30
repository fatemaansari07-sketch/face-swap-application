class AppearanceMatcher:

    def __init__(self):

        print("🎯 Appearance Matcher Loaded!")

    def calculate(
        self,
        lighting_score,
        color_score,
        skin_score,
    ):

        lighting_score = float(
            lighting_score
        )

        color_score = float(
            color_score
        )

        skin_score = float(
            skin_score
        )

        # ------------------------------------------
        # Weighted Appearance Score
        # ------------------------------------------

        final_score = (
            lighting_score * 0.35
            + color_score * 0.30
            + skin_score * 0.35
        )

        final_score = max(
            0.0,
            min(
                100.0,
                final_score,
            ),
        )

        return {

            "lighting": round(
                lighting_score,
                2,
            ),

            "color": round(
                color_score,
                2,
            ),

            "skin": round(
                skin_score,
                2,
            ),

            "final_score": round(
                final_score,
                2,
            ),
        }