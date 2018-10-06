'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        n -= 1
        while n > 0:
            res = ""
            pre = ans[0]
            count = 1
            for i in range(1, len(ans)):
                if pre == ans[i]:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = ans[i]
                    count = 1
            res += str(count) + pre
            ans = res
            n -= 1
        return ans

    def countAndSay1(self, n):    # Time:  O(n * 2^n)  # Space: O(2^n)
        seq = "1"
        for i in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq

    def countAndSay2(self, n):
        oldstr = '1'
        for i in range(n-1):
            tem = ''
            count = 1
            for j in range(1, len(oldstr) + 1):
                if j < len(oldstr) and oldstr[j] == oldstr[j-1]:
                    count += 1
                else:
                    tem += str(count) + oldstr[j-1]
                    count = 1
            oldstr = tem
        return oldstr

if __name__ == "__main__":
    for i in range(1, 4):
        print(Solution().countAndSay2(i))
