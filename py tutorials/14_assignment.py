#             #TASK2
def reward(n):
    if n >= 500 :
        return "GOLD"
    elif n < 500 and n >= 200:
        return "SILVER"
    elif n < 200 and n >= 100:
        return "Bronze"
    else:
        return "Unknown"
#
#             # Task1
# spends = {}
# with open("customer.txt", 'r') as cus:
#     for line in cus:
#         name, spend= line.split(",")
#         spends[name] = int(spend)
#     print(spends)
#
#             # Task3
#
# for name, spend in spends.items():
#     rev = reward(spend)
#     spends[name] = (spend, rev)
# print(spends)


def customer_summary(file_name):
    t_summary = {}
    with open(file_name, "r") as file:

        def award(n):
            if n >= 500:
                return "GOLD"
            elif n < 500 and n >= 100:
                return "SILVER"
            elif n < 200 and n >= 100:
                return "Bronze"
            else:
                return "Unknown"

        for line in file:
            name, spend = line.split(",")
            t_summary[name] = (int(spend), reward(int(spend)))

        print(t_summary)

customer_summary("customer.txt")
