from ai.pipeline.pipeline import AIPipeline


class AIManager:

    def __init__(self):

        print("🚀 Starting AI Manager...")

        self.pipeline = AIPipeline()

        print("✅ AI Manager Ready!")

    def face_swap(
        self,
        source_path=None,
        target_path=None,
        output_path=None,
        left_path=None,
        center_path=None,
        right_path=None,
    ):

        # -------------------------------
        # Multi Identity Mode
        # -------------------------------

        if (
            left_path is not None
            and center_path is not None
            and right_path is not None
        ):

            print("\n🧠 Multi Identity Mode Enabled")

            return self.pipeline.process(
                source_path=center_path,
                target_path=target_path,
                output_path=output_path,
                left_path=left_path,
                center_path=center_path,
                right_path=right_path,
            )

        # -------------------------------
        # Single Identity Mode
        # -------------------------------

        print("\n🙂 Single Identity Mode Enabled")

        return self.pipeline.process(
            source_path=source_path,
            target_path=target_path,
            output_path=output_path,
        )