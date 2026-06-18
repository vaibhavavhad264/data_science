
import os

# f = open("funny.txt", "r")
# for line in f:
#     print(line)
# f.close()

# with open("love.txt", "a") as l:
#     l.write("I love Go-Lang\n")
#     l.write("I love Data")

player_score = {}


with open("scores.csv", "r") as file:
    for line in file:
        total  = 0
        player, match, score = line.split(",")
        score = int(score)
        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player] = [score]
    print(player_score)

    for player, player_s in player_score.items():
        mn = min(player_s)
        mx = max(player_s)
        avg = sum(player_s)/len(player_s)
        print(f"{player} ==> MIN : {mn}, MAX : {mx}, AVG : {avg}")




if os.path.exists("funny.txt"):
    os.remove("funny.txt")
    print("file is removed")
else:
    print("file is not exists")
