'''
# Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", which the length is 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        start, maxsub, hash = 0, 0, {}

        for i, num in enumerate(s):
            # Need to have the following condition:
            # start <= hash[num] to avoid edge case such as :
            # "tmmzuxt"
            if num in hash and start <= hash[num]:
                start = hash[num] + 1
            else:
                maxsub = max(maxsub, i - start + 1)

            hash[num] = i

        return maxsub

    def lengthOfLongestSubstring1(self, s):
        dict = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in dict:
                start = max(start, dict[c] + 1)
            dict[c] = i
            ans = max(ans, i - start + 1)
        return ans

    def lengthOfLongestSubstring2(self, s):
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
