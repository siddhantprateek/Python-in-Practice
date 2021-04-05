try:
    file = open("cleaning_up.py")
    age = int(input("Age:"))
    x_factor = 10 / age

# there are times we have work with external resources like file, network connection ,data bases and so on.
# after we are done we have to release that
# after opening a file we must close it otherwise another may not open it.

# if we close the file before exception  it won't be executed

except (ValueError, ZeroDivisionError):
    print("You didn't enter valid age ")
else:
    print("No exception were thrown")
finally:
    file.close()

# final clause is always executed whether we have exception or not
# and used to release external resources
