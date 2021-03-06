'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])
            maxSum = max(maxSum, preSum)
        return maxSum

    def maxSubArray1(self, nums):
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = 0, 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == "__main__":
    print(Solution().maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
