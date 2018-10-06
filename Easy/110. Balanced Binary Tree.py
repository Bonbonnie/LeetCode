"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(root):
            if root is None:
                return 0
            left_height, right_height = getHeight(root.left), getHeight(root.right)
            if left_height < 0 or right_height < 0 or \
                    abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return getHeight(root) >= 0
    
    def isBalanced1(self, root):
        def deeps(p):
            if not p:
                return 0
            left = deeps(p.left)
            right = deeps(p.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        if deeps(root) == -1:
            return False
        return True


if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.left.right, root.left.left = TreeNode(15), TreeNode(7)
    root.left.left.left, root.left.left.right = TreeNode(3), TreeNode(2)
    print(Solution().isBalanced(root))
