
# Rcursive way
def knapSack(values, weights, capacity):
    return knapSackHelper(values, weights, capacity, 0)

def knapSackHelper(values, weights, capacity, index):
    if capacity <= 0 and index >= len(weights):
        return 0

    profit = 0
    if weights[index] <= capacity:
        profit1 = values[index] + knapSackHelper(value, weights, capacity - weights[index], index + 1)
    # second condition will be won't take the item and won't decrease the capacity
    profit2 = knapSackHelper(value, weights, capacity, index + 1)

    return max(profit1, profit2)


# Dynamic Prog.

def knapSackDP(values, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights))]
    return knapSackDPHelper(values, weights, capacity, 0, dp)

def knapSackDPHelper(values, weights, capacity, index, dp):
    if capacity <= 0 and index >= len(weights):
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = values[index] + knapSackDPHelper(values, weights, capacity - weights[index], index +1 , dp)

    profit2 = knapSackDPHelper(values, weights, capacity, index + 1, dp)
    dp[index][capacity] = max(profit1, profit2)

    return dp[index][capacity]

# iterative method

def kanpSitr(values, weights, capacity):
    if capacity <= 0 and len(weights) == 0 or len(weights) != len(values):
        return 0

    dp = [[None for _ in range(capacity + 1)] for _ in range(len(weights))]

    # for capacity 0 we won't put any values
    for i in range(len(weights)):
        dp[i][0] = 0

    n = len()
    for c in range(capacity + 1):
        # will fill up capacity greater than the weights
        if weights[0] <= c:
            dp[0][c] = values[0] ###
    n = len(weights)
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1 = 0
            if weights[i] <= c:
                profit1 = values[i] + dp[i - 1][c - weights[i]]
            profit2 = dp[i - 1][c]
            dp[i]][c] = max(profit1, profit2)
    # final ans
    return dp[n - 1][capacity]
