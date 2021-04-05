# A parameter is the variable listed inside the parentheses in the function definition.
# IN C : parameter is also called formal parameter
# Formal Parameters are the variables defined by the function that receives values when the function is called.
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


# An argument is the value that are sent to the function when it is called.
# argument is also called actual parameter.
# Actual Parameters are the values that are passed to the function when it is invoked or called.
greet("Siddhant", "Prateek")
