def arrSum(arr, index = 0,first = [], second = [], fsum = 0, ssum = 0):


    if len(arr) == index:
        if fsum == ssum:
            print(first, second)
        return


    first.append(arr[index])
    arrSum(arr, index + 1, first, second, fsum + arr[index], ssum)
    first.pop()

    second.append(arr[index])
    arrSum(arr, index + 1, first, second, fsum, ssum + arr[index])
    second.pop()



nums = [1, 2, 4, 2, 4, 1]
arrSum(nums)


