"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = []
        for r in range(rowIndex):
            arr.append([])
            for n in range(r+1):
                if n in (0, r):
                    arr[r].append(1)
                else:
                    arr[r].append(arr[r-1][n-1] + arr[r-1][n])
        return arr[rowIndex-1]

    def getRow1(self, rowIndex):
        fact = [1] * (rowIndex + 1)
        ans = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            fact[i] = fact[i - 1] * i
        for i in range(1, rowIndex):
            ans[i] = fact[-1] / (fact[i] * fact[rowIndex - i])
        return ans

    def getRow2(self, rowIndex):
        result = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            old = result[0] = 1
            for j in range(1, i + 1):
                old, result[j] = result[j], old + result[j]
        return result

    def getRow3(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row





if __name__ == "__main__":
    print(Solution().getRow3(3))