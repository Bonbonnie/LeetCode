"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        for r in range(numRows):
            arr.append([])
            for n in range(r+1):
                if n in (0, r):
                    arr[r].append(1)
                else:
                    arr[r].append(arr[r-1][n-1] + arr[r-1][n])
        return arr

    def generate1(self, numRows):
        ans = [[1] * n for n in range(1, numRows+1)]
        for i in range(1, numRows + 1):
            for j in range(0, i - 2):
                ans[i-1][j+1] = ans[i-2][j] + ans[i-2][j+1]
        return ans

    def generate2(self, numRows):
        ans = [[1] * n for n in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans


if __name__ == "__main__":
    print(Solution().generate2(5))