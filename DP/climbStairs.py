#Count the no. of moves to climb the stairs
from functools import lru_cache

def number_of_ways_to_top(top: int, max_steps: int) -> int:
    @lru_cache(None)
    def compute_max_no_of_ways(h):
        if h <= 1:
            return 1

        return sum( compute_max_no_of_ways(h - i) for i in range(1, min(max_steps, h) + 1))

    return compute_max_no_of_ways(top)
# top, steps
n, k = 4, 2
print(number_of_ways_to_top(n, k))


# method 2
# it takes O(2^top) time complexity

def countWaysToTop(top, steps):
    if top <= 1:
        return top

    counter = 0
    curr_step_size = 1
    while curr_step_size <= top and curr_step_size <= steps:
        counter += countWaysToTop(top - curr_step_size, steps)
        curr_step_size += 1

    return counter

print("No. of Ways:", countWaysToTop(n + 1, k))

# Method 3 Sliding Window O(n)
def countWays_to_the_top(top, steps):

    temp = 0
    curr_step = [1]

    for i in range(1, top + 1):
        start, end = i - steps - 1, i - 1

        if start >= end:
            temp -= curr_step[start]
        temp += curr_step[end]

        curr_step.append(temp)

    return curr_step[top]

print("No. of Ways:", countWays_to_the_top(n, k))

