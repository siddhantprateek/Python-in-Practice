# the time complexity it takes is O(1.618^n) it is also called the golden retio the quadratic
# equation for it is x2 - x - 1
# in general the complexity is O(2^n) which is bad or worst
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n -1) + fibo(n - 2)

# doing it DP or mamorization

def fiboDP(n, dp):
    if n < 2:
        return n
    if dp[n]:
        return dp[n]
    # mamorization
    dp[n] = fiboDP(n - 1, dp) + fiboDP(n -2, dp)
    return dp[n]
def fiboDP2(n, dp):
    if n < 2:
        return n
    if dp[n]:
        return dp[n]
    # mamorization
    result = fiboDP2(n - 1, dp) + fiboDP2(n -2, dp)
    dp[n] = result
    return dp[n]


ans = []
for i in range(15):
    ans.append(fiboDP(i, [None for _ in range(101)]))
# buttom up approuch
def fiboBU(n):
    if n < 2:
        return n
    #
    f_minus_1, f_minus_2 = 1, 0
    for i in range(2, n + 1):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


result = []
for i in range(15):
    result.append(fiboBU(i))



for i in range(15):
    print(ans[i], end=" ")
print()
for i in range(15):
    print(result[i], end=" ")
