"""
Given a binary tree, write a function to get the maximum width of the given tree.
The width of a tree is the maximum width among all levels.
The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level,
where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, i, depth, leftmosts):
            if not node:
                return 0
            if depth >= len(leftmosts):
                leftmosts.append(i)
            return max(i - leftmosts[depth] + 1,
                       dfs(node.left, i * 2, depth + 1, leftmosts),
                       dfs(node.right, i * 2 + 1, depth + 1, leftmosts))

        leftmosts = []
        return dfs(root, 1, 0, leftmosts)

    def widthOfBinaryTree1(self, root):
        def dfs(root, x, y, num, dmin, dmax):
            if root:
                left = dfs(root.left, x - 1, y + 1, num * 2, dmin, dmax)
                right = dfs(root.right, x + 1, y + 1, 1 + num * 2, dmin, dmax)
                dmin[y] = min(num, dmin.get(y, float("inf")))
                dmax[y] = max(num, dmax.get(y, float("-inf")))
                return max(left or 0, right or 0, 1 + dmax[y] - dmin[y])

        return dfs(root, 0, 0, 1, {}, {})



if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.left.left, root.right.right = TreeNode(15), TreeNode(7)
    print(Solution().widthOfBinaryTree(root))