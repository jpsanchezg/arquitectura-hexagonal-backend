class FormatError(Exception):
    def __init__(self, attribute: str) -> None:
        self.attribute = attribute
        super().__init__(f"Invalid format for {attribute}")
