def maxProfit(price, start, end):

    if start >= end:
        return 0


    profit = 0

    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                currProfit = price[j] - price[i] + maxProfit(price, start, i - 1) + maxProfit(price, j + 1, end)

                profit = max(profit, currProfit)

    return profit

price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)
print(maxProfit(price, 0, n - 1))
