"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):    # Recursive solution
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isLandRSymmetric(root.left, root.right)

    def isLandRSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isLandRSymmetric(left.left, right.right) and self.isLandRSymmetric(left.right, right.left)

    def isSymmetric1(self, root):
        def helper(root, mirror):
            if not root and not mirror:
                return True
            if root and mirror and root.val == mirror.val:
                return helper(root.left, mirror.right) and helper(root.right, mirror.left)
            return False
        return helper(root, root)

    def isSymmetric2(self, root):     # Iterative solution
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            r, l = stack.pop(), stack.pop()
            if r is None and l is None:
                continue
            if r is None or l is None or r.val != l.val:
                return False

            stack.append(r.left)
            stack.append(l.right)
            stack.append(r.right)
            stack.append(l.left)

        return True







if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print(Solution().isSymmetric2(root))
