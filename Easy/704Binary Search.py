"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r -= 1
            elif nums[mid] < target:
                l += 1
            else:
                return mid
        return -1

