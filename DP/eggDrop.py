import math

def eggDrop(egg, floor):
    if floor == 0:
        return 0
    # if only egg we had and start from the bottom the
    if egg == 1:
        return floor

    ans = math.inf
    for i in range(1, floor + 1):
        sol = max(eggDrop(egg - 1, i - 1), eggDrop(egg, floor - i)) + 1
        ans = min(ans, sol)

    return ans
print(eggDrop(2, 10))

#DP
def eggDropDP(egg, floor):
    dp = [[None for _ in range(floor + 1)] for _  in range(egg + 1)]
    return eggDropDPH(egg, floor, dp)
def eggDropDPH(egg, floor, dp):
    if floor == 0:
        return 0

    if egg == 1:
        return floor

    if dp[egg][floor]:
        return dp[egg][floor]

    ans = math.inf

    for i in range(1, floor + 1):
        sol = max(eggDropDPH(egg - 1, i - 1, dp), eggDropDPH(egg, floor -i, dp)) + 1
        ans = min(sol, ans)

    dp[egg][floor] = ans
    return dp[egg][floor]

print(eggDropDP(2, 10))

# ITR
def eggDropITR(eggs, floors):
    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]

    for i in range(eggs + 1):
        dp[i][0] = 0

    for flr in range(floors + 1):
        dp[1][flr] = flr

    for egg in range(1, eggs + 1):
        for flr in range(0, floors + 1):
            ans = math.inf
            for i in range(1, flr + 1):
                sol = max(dp[egg - 1][i - 1], dp[egg -1][flr - i]) + 1
                ans = min(ans, sol)

            dp[egg][flr] = ans

    return dp[eggs][floors]
print(eggDropITR(2, 10))
