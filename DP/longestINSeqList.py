def findLongestINSeq(nums):

    dp = [[] for _ in range(len(nums))]
    # dp[0] denotes the longest increasing subsequence ending at nums[0]
    dp[0].append(nums[0])

    for i in range(1, len(nums)):

        for j in range(i):

            if nums[j] < nums[i] and len(dp[j]) > len(dp[i]):
                dp[i] = dp[j].copy()

        dp[i].append(nums[i])

    j = 0
    for i in range(len(nums)):
        if len(dp[j]) < len(dp[i]):
            j = i

    print(dp[j])

nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
findLongestINSeq(nums)
