from datetime import datetime

import datetime

class Cricket_Player:
    def __init__(self, f_name, l_name, birt_year, team_name):
        self.f_name = f_name
        self.l_name = l_name
        self.birth_year = birt_year
        self.team_name = team_name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores) / len(self.scores)

    def age(self):
        return datetime.date.today().year - self.birth_year

    def __add__(self, other):
        print(f"Name : {self.f_name}    \t No Of Matches : {len(self.scores)} \tTotal Score : {sum(self.scores)} \tAverage Score : {self.get_avg_score()}")
        print(f"Name : {other.f_name}    \t No Of Matches : {len(other.scores)} \tTotal Score : {sum(other.scores)} \tAverage Score : {other.get_avg_score()}")
        print(f"Name : {self.f_name}&{ other.f_name} No Of Matches : {len(self.scores) + len(other.scores)} \tTotal Score : {sum(self.scores) + sum((other.scores))}  \tAverage Score : {(self.get_avg_score() + other.get_avg_score()) / 2 }")

virat = Cricket_Player("Virat", "Kohali", 1988, "INDIA")
virat.add_score(70)
virat.add_score(87)
virat.add_score(78)

rohit = Cricket_Player("Rohit", "Sharam", 1985, "INDIA")
rohit.add_score(77)
rohit.add_score(89)
rohit.add_score(91)

print(virat + rohit)
print(rohit + virat)