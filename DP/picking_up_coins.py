from functools import lru_cache

def maximum_revenue(coins):
    @lru_cache(None)
    def compute_maximum_revenue_for_range(a, b):
        if  a > b:
            return 0


        max_revenue_a = coins[a] + min(
            compute_maximum_revenue_for_range(a + 2, b),
            compute_maximum_revenue_for_range(a + 1, b - 1))
        max_revenue_b = coins[b] + min(
            compute_maximum_revenue_for_range(a + 1, b- 1),
            compute_maximum_revenue_for_range(a, b - 2))
        return max(max_revenue_a, max_revenue_b)

    return compute_maximum_revenue_for_range(0, len(coins) - 1)

# the function is computed O(n^2) times
coins = [4, 5, 6, 8, 1, 7]
print(maximum_revenue(coins))
