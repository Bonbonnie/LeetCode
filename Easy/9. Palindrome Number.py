'''
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 0:
            rev = int(str(x)[::-1])
            return rev == x
        else:
            return False

    def isPalindrome1(self, x):    # Time:  O(1)  # Space: O(1)
        if x < 0:
            return False

        temp, rev = x, 0
        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10
        return rev == x

    def isPalindrome2(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):    #排除100、110等最后一位是0的数
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


if __name__ == "__main__":
    print(Solution().isPalindrome2(12321))
    print(Solution().isPalindrome2(10000))
    print(Solution().isPalindrome2(-12321))

