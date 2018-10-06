"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            queue = deque([(root, root.val)])
            while queue:
                p, s = queue.popleft()
                left, right = p.left, p.right
                if left:
                    queue.append((p.left, s + p.left.val))
                if right:
                    queue.append((p.right, s + p.right.val))
                if not left and not right and s == sum:
                    return True
            return False

        return False

    def hasPathSum2(self, root, sum):
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum2(root.left, sum - root.val) or self.hasPathSum2(root.right, sum - root.val)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.right = TreeNode(2)
    print(Solution().hasPathSum(root, 22))