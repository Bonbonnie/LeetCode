'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution(object):
    def climbStairs(self, n):  # Time:  O(2^n)  # Space: O(n)
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs1(self, n):
        pre, cur = 0, 1
        for i in range(n):
            pre, cur = cur, pre + cur
        return cur

    def climbStairs2(self, n):
        if n <= 1:
            return 1
        pre, cur = 1, 1
        for i in range(2, n + 1):
            pre, cur = cur, pre + cur
        return cur



if __name__ == "__main__":
    result = Solution().climbStairs2(3)
    print(result)