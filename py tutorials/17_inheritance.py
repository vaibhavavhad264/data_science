
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_score(self, runs):
        return runs

class Game(Player):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = "Vaibhav"

KhoKho = Game("Virat", 38)
print(KhoKho.name)
print(KhoKho.age)

