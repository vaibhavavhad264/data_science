def vol_cylinder(radius, height):
    return 3.12* (radius**2) * height
# print(vol_cylinder(5, 5))
# print(vol_cylinder(2, 6))
            ###
# def sum_all(*args):
#     return sum(args)
#
# print(sum_all(1, 2, 3, 4, 5, 6))

            ###
def company_info(**kargs):
    for key in kargs:
        print(key, kargs[key])


company_info(a = "APPL", b = "TIM", c = "CYL", d = 20)

a1 = lambda a : a**2
print(a1(10))
