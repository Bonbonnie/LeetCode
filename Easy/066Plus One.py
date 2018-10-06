'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        digits = digits[::-1]
        for i in range(len(digits)):
            p1 = digits[i] + carry
            carry, digits[i] = divmod(p1, 10)
        if carry:
            digits.append(carry)
        return digits[::-1]

    def plusOne1(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

    def plusOne2(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            digit = (digits[i] + carry) % 10
            carry = 1 if digit == 0 else 0
            digits[i] = digit
        if carry:
            return [1] + digits
        return digits



if __name__ == "__main__":
    print(Solution().plusOne1([9, 9, 9, 9]))
    print(Solution().plusOne1([1, 2, 3, 4]))