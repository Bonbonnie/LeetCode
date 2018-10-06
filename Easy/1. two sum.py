'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):   # Time:  O(n^2)   Space: O(1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[j] == nums[i]:
                    return [i, j]

    def twoSum1(self, nums, target):     #Time:  O(n)   Space: O(n)
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                return [index, dict[target - num]]
            else:
                dict[num] = index

    def twoSum2(self, nums, target):
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            dic[target - num] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target) == [0, 1])

