def mergeSort(nums):

    if len(nums) == 1:
        return nums

    mid = len(nums) // 2

    leftList = mergeSort(nums[:mid])
    rightList = mergeSort(nums[mid:])

    return mergeSorting(leftList, rightList)

def mergeSorting(leftList, rightList):

    result = []
    leftCrusor, rightCrusor  = 0, 0
    while leftCrusor < len(leftList) and rightCrusor < len(rightList):

        if leftList[leftCrusor] > rightList[rightCrusor]:
            result.append(rightList[rightCrusor])
            rightCrusor += 1
        else:
            result.append(leftList[leftCrusor])
            leftCrusor += 1

    result.extend(leftList[leftCrusor:])
    result.extend(rightList[rightCrusor:])

    return result

nums = [4, 6, 1, 7, 2, 8, 12]
print(nums)
print(mergeSort(nums))
