'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, pdict = [], {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in pdict:
                stack.append(p)
            elif len(stack) == 0 or pdict[stack.pop()] != p:
                return False
        return len(stack) == 0

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = ["()", "[]", "{}"]
        for i in range(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2] + stack[-1] in d:
                stack.pop()
                stack.pop()
        return len(stack) == 0

    def isValid2(self, s):
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')':
                if not stack or stack.pop() != '(':
                    return False
            if char == ']':
                if not stack or stack.pop() != '[':
                    return False
            if char == '}':
                if not stack or stack.pop() != '{':
                    return False

        if stack:
            return False
        return True

if __name__ == "__main__":
    print(Solution().isValid1("()[]{}"))
    print(Solution().isValid1("()[{]}"))