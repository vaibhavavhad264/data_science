
#
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     global c
#     c = a / b
# # except ZeroDivisionError as ze:
# #     print("Error occurred :",ze)
# #     c = -1
# # except ValueError as ve:
# #     print("Error occurred :", ve)
# #     c = -1
# except Exception as e:                      # Its not good way to except the error
#     print("Error occurred :", e)



try:
    global ch
    ch = open("C:\\code\\py tutorials\\customer.txt", "r")
    ct = ch.read()
    print(ct)
except FileNotFoundError as fe:
    print("Problem Handel :" , fe)
finally:
    if ch:
        ch.close()
    print("File Closed!")