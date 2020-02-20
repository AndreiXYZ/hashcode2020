class Book:
    def __init__(
        self,
        id: int,
        score: int):
        self.id = id
        self._score = score
    
    def __repr__(self):
        return 'ID= {} Score={}'.format(self.id, self._score)