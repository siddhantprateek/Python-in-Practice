items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# IF YOU WANT TO FILTER THE LIST AND ONLY WANTED ITEM GREATER THAN 10
# of MAKE A LIST FILTERED =  []

# OR
# FILTER FXN TAKES 2 PARAMETERS
#                       v(LAMBDA FXN) v(TAKES BOOLEAN VALUE)< WE PASS OUR FILTER LIST
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)  # ITEM MATCHES THE  ^  CRITERIA OR NOT
