"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
import collections

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum = ans = 0
        visit = {0: 1}
        for i, n in enumerate(nums):
            preSum += n
            ans += visit.get(preSum - k, 0)
            visit[preSum] = visit.get(preSum, 0) + 1
        return ans

    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = collections.defaultdict(int)
        d[0] = 1
        sum = 0
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2]
    k = 2
    print(Solution().subarraySum1(nums, k))