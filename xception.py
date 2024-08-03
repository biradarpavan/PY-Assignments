class DataCleaningError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FileHandlingError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)