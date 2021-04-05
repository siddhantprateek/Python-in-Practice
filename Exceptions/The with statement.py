try:
    with open("p.py") as file:
        # we can work  with this file , we can read or write with it
        print("File Opened.")
        file.__exit__
    age = int(input("Age:"))
    x_factor = 10 / age

except (ValueError, ZeroDivisionError):
    print("You didn't enter valid age ")
else:
    print("No exception were thrown")
