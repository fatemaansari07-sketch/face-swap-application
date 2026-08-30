class ParserUtils:

    def __init__(self):

        print("🛠 Parser Utils Loaded!")

    def get_available_parts(self, parts):

        return [
            name
            for name, value in parts.items()
            if value
        ]

    def has_hair(self, parts):

        return parts.get(
            "hair",
            False,
        )

    def has_glasses(self, parts):

        return parts.get(
            "glasses",
            False,
        )