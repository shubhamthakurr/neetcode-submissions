class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = -1
        res = 0

        for i in range(len(prices)-1,-1,-1):
            max_val = max(max_val, prices[i])
            res = max(res, max_val - prices[i])

        return res