class Book:
    def __init__(
        self,
        id: int,
        score: int):
        self.id = id
        self._score = score