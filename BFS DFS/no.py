def matchingStrings(strings, queries):

    freq = {}
    # for item in strings:
    #     print(item)
    #     if item in queries:
    #         freq[item] = freq.get(item, 0) + 1
    #     else:
    #         freq[item] = 0
    # for item in 

    # print(freq)
    # result = []
    # for val in freq.values():
    #     result.append(val)
    # print(result)
def cookies(k, A):
    #
    # Write your code here.
    #
    mini = 0
    import heapq as hp

    hp.heapify(A)

    while k > mini:
        least1 = hp.heappop(A)
        least2 = hp.heappop(A)
        sweatness = 1*least1 + 2*least2
        hp.heappush(A, sweatness)
        mini = A[0]

    return list(A)

print(cookies(9, [1, 2, 3, 9, 10, 12]))