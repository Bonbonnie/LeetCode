'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = abs(len(a) - len(b))
        maxlen = max(len(a), len(b))
        if len(a) > len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a
        rea = a[::-1]
        reb = b[::-1]
        carry = 0
        bsum = ''
        for i in range(maxlen):
            if carry:
                if rea[i] == reb[i]:
                     bsum += '1'
                     if rea[i] == '0':
                         carry = 0
                else:
                    bsum += '0'
            else:
                if rea[i] == reb[i]:
                    bsum += '0'
                    if rea[i] == '1':
                        carry = 1
                else:
                     bsum += '1'
        if carry:
            bsum += '1'
        return bsum[::-1]

    def addBinary1(self, a, b):
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]

    def addBinary2(self, a, b):
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a

        ret = ""
        carry = 0
        ai, bi = len(a) - 1, len(b) - 1
        al, bl = len(a), len(b)
        while ai >= 0 and bi >= 0:
            ac, bc = a[ai], b[bi]
            if ac == "1" and bc == "1":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 1
            elif ac == "0" and bc == "0":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 0
            else:
                if carry == 1:
                    ret += "0"
                else:
                    ret += "1"

            ai -= 1
            bi -= 1

        if carry == 1:
            ret += "1"
        return ret[::-1]

if __name__ == "__main__":
    a, b = '1010', '1011'
    c, d = "11", "1"
    print(Solution().addBinary(c, d))
