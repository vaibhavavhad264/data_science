exp1 = [45, 67, 234, 22, 45, 66, 33]
exp2 = [34, 23, 22, 45, 66, 67, 45]

def t_exp(n):
    '''
    ___
    :param n: input list containing numbers
    :return: total sum of sll numbers
    '''
    total = 0
    for i in n:
        total += i
    print(total)

t_exp(exp1)
t_exp(exp2)
print(help(t_exp))