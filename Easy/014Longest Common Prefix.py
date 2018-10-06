'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        com = ''
        for i in range(len(strs[0])):
            c = 0
            for j in range(len(strs)-1):
                if strs[j+1][i] == strs[0][i]:
                    c += 1
            if c == len(strs) - 1:
                com += strs[0][i]
        return com

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix2(self, strs):
        if len(strs) == 0:
            return ""
        i = 0
        j = 0
        end = 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]
            else:
                if strs[j][i] != char:
                    break

            if j == len(strs) - 1:
                i += 1
                j = 0
                end += 1
            else:
                j += 1

        return strs[j][:end]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix2(["hello", "heaven", "heavy"]))