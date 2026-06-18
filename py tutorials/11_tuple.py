# def find_pe_ratio_pb_ratio(price, eps, book_value):
#     pe = price/eps
#     pb = price/book_value
#     return pe, pb
#
# pe_ratio, pe_pb = find_pe_ratio_pb_ratio(100, 2, 4)
# print(pe_ratio, pe_pb)

appl_revenue = {
    "USA" : {
        "iPhone" : 20,
        "iPad" : 12,
        "MacBook" : 8
    },
    "China" : {
        "iPhone" : 17,
        "iPad" : 9,
        "MacBook" : 6
    },
    "India" : {
        "iPhone" : 9,
        "iPad" : 4,
        "MacBook" : 3
    }
}

for country, product in appl_revenue.items():
    for product, revenue in product.items():
        print(f"{country} -> {product} -> {revenue} million $")

print(help(appl_revenue))