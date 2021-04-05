from pprint import pprint
#   ^ module
sentence = "This is a common interview question"

# Dictionary is useful as it is collection of key value pair

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

# how to sort it
# a dictionary are un order pairs we cannot sort them
# so we have take each key value pair and convert it into tuple and put it in a list

# char_frequency_sorted = sorted(
#     char_frequency.items(),
#     key=lambda kv: kv[1],
#     reverse=True)

# print(char_frequency_sorted[0])
