exp = [12000, 13000, 14000, 15000, 17000]
m = 0
# for i in range(len(exp)):
#     print(i+1, exp[i])

for i, exp1 in enumerate(exp):
    print(f"Month : {i+1}, Expense : {exp1}")
    m += exp1
print(f"Total Month : {i+1}, Total Expense : {m}")


