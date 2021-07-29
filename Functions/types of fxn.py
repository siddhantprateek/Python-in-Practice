def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Siddhant")
# open("<name of the file>" , "<code>")  "w" to write "r" read
file = open("content.txt", "w")
file.write(message)
