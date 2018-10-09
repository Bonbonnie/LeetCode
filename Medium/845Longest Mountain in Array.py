"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)
Given an array A of integers, return the length of the longest mountain.
Return 0 if there is no mountain.

Example 1:
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000
"""


class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(A)-1):
            ll, rr = i-1, i+1
            lr = rl = i
            while A[ll] < A[lr]:
                ll -= 1
                lr -= 1
            while A[rl] > A[rr]:
                rl += 1
                rr +=1
            if rl-lr+1 >= 3:
                res = max(res, (rl-lr+1))
        return res

    def longestMountain1(self, A):
        result, up_len, down_len = 0, 0, 0
        for i in range(1, len(A)):
            if (down_len and A[i - 1] < A[i]) or A[i - 1] == A[i]:
                up_len, down_len = 0, 0
            up_len += A[i - 1] < A[i]
            down_len += A[i - 1] > A[i]
            if up_len and down_len:
                result = max(result, up_len + down_len + 1)
        return result

if __name__ == "__main__":
    A = [2, 1, 4, 7, 3, 2, 5]
    B = [2, 2, 2]
    print(Solution().longestMountain1(A))