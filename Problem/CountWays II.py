# Recursive Approuch
def countWays(Stairs, step):

    if Stairs < 0:
        return 0
    if Stairs == 0:
        return 1

    count = 0
    for i in range(1, step + 1):
        StairsLeft = Stairs - i
        count += countWays(StairsLeft, step)

    return count


# while True:
#     stairs = int(input("stairs >>" ))
#     steps = int(input("steps >>"))
#
#     print("Total Ways: ", countWays(stairs, steps))
#
#     if stairs == 0:
#         break


# DP Top buttom Approuch
def CountWaysDP(Stairs, step, dp):

    if Stairs < 0:
        return 0

    if Stairs == 0:
        return 1

    if dp[Stairs] == 0:

        for i in range(1, step + 1):
            dp[Stairs] += CountWaysDP(Stairs -i, step, dp)

    return dp[Stairs]

def CountWaysDPfinder():
    n = int(input(">>"))
    m = 3
    dp = [0 for _ in range(n + 1)]

    print("Ways:", CountWaysDP(n, m, dp))

CountWaysDPfinder()
