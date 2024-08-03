class alreadyexception(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class notfoundexception(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class quantityexception(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
