def mergeSort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    leftList = mergeSort(nums[:mid])
    rightList = mergeSort(nums[mid:])
    return mergeSorting(leftList, rightList)


def mergeSorting(leftList, rightList):
    leftCursor, rightCursor = 0, 0
    result = []
    while leftCursor < len(leftList) and rightCursor < len(rightList):
        if leftList[leftCursor] < rightList[rightCursor]:
            result.append(leftList[leftCursor])
            leftCursor += 1
        else:
            result.append(rightList[rightCursor])
            rightCursor += 1

    result.extend(leftList[leftCursor:])
    result.extend(rightList[rightCursor:])
    return result


print(mergeSort([4, 5,1,2, 7, 9, 8]))