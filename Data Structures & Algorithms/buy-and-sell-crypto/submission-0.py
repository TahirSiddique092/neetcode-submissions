class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)-1):
            buyP = prices[i]
            sellP = max(prices[i+1:])
            maxP = max(sellP-buyP, maxP)
        return maxP
        