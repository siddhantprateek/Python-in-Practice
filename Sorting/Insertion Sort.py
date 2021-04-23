"""
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
Worst complexity: n^2
Average complexity: n^2
Best complexity: n
Space complexity: 1
Method: Insertion
Stable: Yes
Class: Comparison sort
"""

# INSERTION SORT IS NOT FAST SORTING ALGORITHM BECAUSE IT USES IT USES NESTED LOOPS  TO SORT
# IT IS USEFUL  ONLY FOR SMALL DATA SETS
# IT RUNS IN n^2


def insertion_sort(A):
    """Method 1"""
    # for i in range(1, len(A)):
    #     for j in range(i-1, -1, -1):
    #         if A[j] > A[j+1]:
    #             A[j], A[j+1] = A[j+1], A[j]
    #         else:
    #             break

    # or By using while loop
    """Method 2"""

    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1



    """ Method 3"""
    # wrong
    # for i in range(1, len(A)):
    #     currentNum = A[i]
    #     for j in range(i-1, 0, -1):
    #         if A[j] > currentNum:
    #             A[j+1] = A[j]
    #         else:
    #             A[j+1] = currentNum
    #             break
    #
    return A

print(insertion_sort([9, 4, 5, 6, 2, 3, 1]))
