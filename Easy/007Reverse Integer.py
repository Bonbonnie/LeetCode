'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
# Time:  O(logn) = O(1)
# Space: O(1)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        rev = 0 if abs(rev) > 0x7fffffff else rev
        return rev

    def reverse1(self, x):
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        return sign * ans if ans <= 0x7fffffff else 0

if __name__ == "__main__":
    print(Solution().reverse1(123))
    print(Solution().reverse1(-321))