items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# items.sort()
# print(items)


# AS WE SEE ITEM ARE NOT SORTED
# PYTHON DOESN'T KNOW HOW TO SORT THIS LIST
# SO DEFINE A FXN

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
