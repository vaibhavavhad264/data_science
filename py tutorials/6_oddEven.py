print("Hello World")
n = int(input("Enter the number : "))
        # Popular way
# if n % 2 == 0:
#     print(f"The {n} is even number.")
# else:
#     print(f"The {n} is odd number.")


        # New Way - Ternary operator
mess = f"The {n} is odd." if n%2 == 1 else f"The {n} is even"
print(mess)
