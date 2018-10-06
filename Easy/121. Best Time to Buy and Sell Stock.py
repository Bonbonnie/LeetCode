"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for s in range(1, len(prices)):
            for b in range(s):
                m = prices[s] - prices[b]
                res = max(res, m)
        return res

    def maxProfit1(self, prices):
        if not prices:
            return 0
        ans = 0
        pre = prices[0]
        for i in range(1, len(prices)):
            pre = min(pre, prices[i])
            ans = max(prices[i] - pre, ans)
        return ans


if __name__ == "__main__":
    p = [7, 1, 5, 3, 6, 4]
    p2 = [7, 6, 4, 3, 1]
    p1 = []
    print(Solution().maxProfit1(p1))