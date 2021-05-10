# Recurssive
def longestCommon(s1: str, s2: str):
    return findLengthoflongestSeq(s1, s2, len(s1), len(s2))

def findLengthoflongestSeq(s1, s2, l1, l2):

    if l1 == 0 or l2 == 0:
        return 0

    if s1[l1 - 1] == s2[l2 - 1]:
        return findLengthoflongestSeq(s1, s2, l1 - 1, l2 - 1) + 1

    return max(findLengthoflongestSeq(s1, s2, l1, l2 - 1), findLengthoflongestSeq(s1, s2, l1 - 1, l2))



X = "ABCBDAB"
Y = "BDCABA"

print(longestCommon(X, Y))


# DP

def lCSlength(s1, s2, m, n, lookup):

    if m == 0 or n == 0:
        return 0

    key = (m, n)
    if key not in lookup:

        if s1[m - 1] == s2[n - 1]:
            lookup[key] = lCSlength(s1, s2, m- 1, n - 1, lookup) + 1
        else:
            lookup[key] = max(lCSlength(s1, s2, m, n - 1, lookup), lCSlength(s1, s2, m- 1, n, lookup))

    return lookup[key]

lookup = {}
print(lCSlength(X, Y, len(X), len(Y), lookup))
