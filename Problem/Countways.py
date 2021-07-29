"""
Count ways to reach the nth stair using step 1, 2 or 3
"""

def findSteps(n : int) -> int:

    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return findSteps(n - 1) + findSteps(n - 2) + findSteps(n - 3)

while True:
    n = int(input(">>"))
    print(findSteps(n ))
    if n == None:
        break
