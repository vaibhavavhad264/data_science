
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_score(self, runs):
        return runs

class Game(Player):
    def __init__(self, name, age, matches_played):
        super().__init__(name, age)
        self.matches_played = matches_played
        # self.name = "Vaibhav"

KhoKho = Game("Virat", 38, 200)
print(KhoKho.name)
print(KhoKho.age)
print(KhoKho.matches_played)

