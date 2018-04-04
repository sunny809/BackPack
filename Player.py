class Player:
    def __init__(self, _id, _name, _age, _score):
        self.name = _name
        self.age = _age
        self.score = _score

    def __str__(self):
        return "Player:id[" + self.id + "]name[" + self.name + "],age[" + self.age + "],score[" + self.score + "]"
