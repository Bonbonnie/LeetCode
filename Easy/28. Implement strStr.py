'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class Solution(object):
    def strStr(self, haystack, needle):     # Time:  O(n * k)  # Space: O(k)
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:   # Time:  O(n * k)  # Space: O(k)
            return 0
        if len(haystack) > len(needle):
            for i in range(len(haystack)-len(needle)):
                if haystack[i:i + len(needle)] == needle:
                    return i
            return -1
        return 0 if needle == haystack else -1

    def strStr1(self, haystack, needle):
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(0, len(haystack)):
            k = i
            j = 0
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == len(needle):
                return i
        return -1 if needle else 0


if __name__ == "__main__":
    print(Solution().strStr1("a", ""))
    print(Solution().strStr1("aaaaa", "b"))
    print(Solution().strStr1("hello", "ll"))
