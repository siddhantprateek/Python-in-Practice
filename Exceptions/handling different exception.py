try:
    age = int(input("Age:"))
    x_factor = 10 / age

# except ValueError:
#     print("You didn't enter valid age ")
# except ZeroDivisionError:
#     print("You didn't enter valid age ")

# can written in one line

except (ValueError, ZeroDivisionError):
    print("You didn't enter valid age ")

else:
    print("No exception were thrown")
