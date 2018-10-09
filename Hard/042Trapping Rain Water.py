"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = left = 0
        right = len(height) - 1
        leftWall = rightWall = float("-inf")
        while left <= right:
            if leftWall <= rightWall:
                ans += max(0, leftWall - height[left])
                leftWall = max(leftWall, height[left])
                left += 1
            else:
                ans += max(0, rightWall - height[right])
                rightWall = max(rightWall, height[right])
                right -= 1
        return ans

    def trap1(self, A):
        result = 0
        top = 0
        for i in range(len(A)):
            if A[top] < A[i]:
                top = i

        second_top = 0
        for i in range(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        second_top = len(A) - 1
        for i in reversed(range(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        return result

    def trap2(self, A):
        result = 0
        stack = []

        for i in range(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += (min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height

                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])

        return result

if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
