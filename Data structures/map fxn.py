items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


# prices = []
# for item in items:
#     prices.append(item[1])


x = map(lambda item: item[1], items)
for item in x:
    print(item)


prices = list(map(lambda item: item[1], items))
print(prices)
