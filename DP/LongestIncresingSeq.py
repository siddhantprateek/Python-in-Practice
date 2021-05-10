

import sys

def longestInSeq(nums, index, length, prev):

    # Base case
    # if nothing is remaining
    if index == length:
        return 0

    # Case 1: exclude the current element and process the remaining elements
    exclude = longestInSeq(nums, index + 1, length, prev)

    # Case 2: include the current element if it is greater them the previous element in the LIS
    include = 0
    if nums[index] > prev:
        include = 1 + longestInSeq(nums, index + 1, length, nums[index])

    return max(include, exclude)


nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
index, length = 0, len(nums)

# python sys module provides functions and variables which are
# used to manipulate different parts of the Python Runtime Environment.

print(longestInSeq(nums, index, length, -sys.maxsize))na
