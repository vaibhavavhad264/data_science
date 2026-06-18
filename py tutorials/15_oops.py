import datetime
def average_Score(player):
    return sum(player["Score"]) / len(player["Score"])

def get_age(player):
    return datetime.date.today().year - player["Birth"]


virat = {
    "First" : "Virat",
    "Last" : "Kohli",
    "Score" : [],
    "Birth" : 1988
}

virat["Score"].append(100)
virat["Score"].append(100)
virat["Score"].append(0)

print(average_Score(virat))
print(get_age(virat))
print(datetime.date.today().year)