number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":  # command whatever case upper or lower it will convert it into lower case and terminate the programme
    command = input(">")
    print("ECHO", command)
