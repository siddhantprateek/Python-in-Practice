count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(f"{number} is even")
        count += 1
        print(f"total {count} even numbers")
    else:
        print(f"{number} is odd")
