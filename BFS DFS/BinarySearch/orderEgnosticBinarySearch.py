# order agnostic binary search

def bs(arr, target):

    start, end =  0, len(arr) - 1
    isAsc = arr[start] < arr[end]
    while start <= end:
        # not to overflow, it is more efficient or fast
        mid = start + (end -start) // 2

        if target == arr[mid]:
            return mid

        if isAsc:
            if target < arr[mid]:
                end = mid - 1
            if target > arr[mid]:
                start = mid + 1
        else:
            if target < arr[mid]:
                start = mid + 1
            if target > arr[mid]:
                end = mid - 1
# binart search in recursion method:
# n = len(arr)
def binartSearchRec(arr, target, start = 0, end = 0):
    if start > end:
        return -1
    mid = start + (end - start) // 2

    if target == arr[mid]:
        return mid
    if target < arr[mid] :
        return binartSearchRec(arr, target, start, mid - 1)
    return binartSearchRec(arr, target, mid + 1, end)

arr = [1,2,4,7,8,9]
n = len(arr)
print("binartSearchRec: ", binartSearchRec(arr, 7, 0, n - 1))






# ceiling of a number
def ceiling(arr, target):
    if target > arr[-1]:
        return -1

    start, end = 0, len(arr) - 1

    while start <= end:

        mid = start + (end - start)// 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return start

# find the range of number of target spread in the list
def findtherange(arr, target):
    result = [-1,-1]

    result[0] = BS(arr, target, False)
    if result[0] != -1:
        result[1] = BS(arr, target, True)
    return result

def BS(arr, target, findRightIndex):
    index = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            index = mid

            if findRightIndex:
                start = mid + 1
            else:
                end = mid - 1
    return index

print(findtherange([1,3,5,8,8,8,8,7,9], 8))

def rangeofInfiniteArr(arr):
    pass


# find pivot in bitonic array
def findPivot(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return end

print(findPivot([1,3,5,8,7,2,2]))

# make pivot of rotated binary search
# solve rotated binary search with pivot
def pivotIn_rotated(arr, target):
    start, end = 0, len(arr) - 1
    pivot = getpivot(arr, start, end)
    if pivot == -1:
        return binarySearch(arr, target)

    if arr[pivot] == target:
        return pivot
    if arr[0] <= target:
        return binarySearch(arr[:pivot], target)
    return pivot + binarySearch(arr[pivot:], target)

def getpivot(arr, start, end):

    if start > end:
        return -1
    if start == end:
        return start
    mid = start + (end - start) // 2

    if mid < end and arr[mid] > arr[mid + 1]:
        return mid
    if mid > start and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[start] >= arr[mid]:
        return getpivot(arr, start, mid - 1)
    return getpivot(arr, mid + 1, end)


def binarySearch(arr, target):
    index = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid

    # def findPivotRotated(arr):
    #
    #     while start <= end:
    #         mid = start + (end - start) // 2
    #
    #         if arr[mid] > arr[mid + 1] and mid <start :
    #             return mid
    #         if arr[mid] < arr[mid - 1]:

print("pivotIn_rotated:", pivotIn_rotated([4,5,6,1,2,3], 5))
print("pivotIn_rotated:", pivotIn_rotated([4,5,6,1,2,3], 3))
print("pivotIn_rotated:", pivotIn_rotated([4,5,6,1,2,3], 2))



# solve rotated binary search without pivot


# Q: Find the Rotation Count in Rotated Sorted array
def RotationCount(arr):
    # position of pivot + 1 is the no. of rotation in
    start, end = 0, len(arr) - 1
    return 1 + pivotRot(arr, start, end)


def pivotRot(arr, start, end):

    if start > end:
        return -1
    if start == end:
        return start

    mid = start + (end - start) // 2

    if mid < end  and arr[mid] >  arr[mid + 1]:
        return mid
    if mid > start and arr[mid] < arr[mid - 1]:
        return mid - 1

    # allocating the position pivot
    # if mid is in another incresing list
    if arr[start] >= arr[mid]:
        return pivotRot(arr, start, mid - 1)
    # if mid is in ratated part
    return pivotRot(arr, mid + 1, end)

print("RotationCount:", RotationCount([4,5,6,7, 1, 2,3]))

def pivot_of_Rotated(arr):

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        # if mid is greater the next elemnt then it is the pivot
        if start < mid and arr[mid] < arr[mid - 1]:
            return mid - 1
        # if mid is ammler tgan prev element then preb element is the pivot
        elif mid < end and arr[mid] > arr[mid + 1]:
            return mid
        else:
            # the pivot will lie on the unsorted side
            if arr[start] >= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1
print("without rec:",pivot_of_Rotated([4,5,7,9,10,-1,2]))


def get_pivot_ofRotatedArr(arr):

    start, end = 0, len(arr) -1

    while start <= end:

        mid = start + (end - start) // 2

        if start < mid and arr[mid] < arr[mid - 1]:
            return mid
        elif mid < end  and arr[mid] > arr[mid + 1]:
            return mid - 1
        else:
            if arr[start] >= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1
