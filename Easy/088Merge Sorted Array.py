'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):  # Time:  O(n)  # Space: O(n)
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

    def merge1(self, A, m, B, n):   # Time:  O(n)  # Space: O(1)
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1

        while j >= 0:
            A[last] = B[j]
            last, j = last - 1, j - 1

    def merge2(self, nums1, m, nums2, n):
        end = m + n - 1
        m -= 1
        n -= 1
        while end >= 0 and m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end] = nums2[n]
                n -= 1
            end -= 1

        while n >= 0:
            nums1[end] = nums2[n]
            end -= 1
            n -= 1

if __name__ == "__main__":
    A = [2, 3, 5, 0, 0, 0, 0]
    B = [1, 4, 6, 7]
    Solution().merge(A, 3, B, 4)
    print(A)



