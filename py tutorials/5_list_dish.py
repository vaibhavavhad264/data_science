indian = [1, 3, 5, 7, 9]
chinese = [0, 2, 4, 6]
italian = [11, 22, 33, 44, 55, 66, 77]

dish = int(input("Enter the number : "))

if dish in indian:
    print(f"{dish} is Indian.")
elif dish in chinese:
    print(f"{dish} is Chinese.")
elif dish in italian:
    print(f"{dish} is Italian.")
else:
    print(f"{dish} is not a known dish.")