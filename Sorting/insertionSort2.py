def insertionSort(array):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [9, 4, 5, 6, 2, 3, 1]
insertionSort(array)
print(array)
