"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result[::-1]

    def levelOrderBottom1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = [[root.val]]
        queue = deque([root])
        while queue:
            levelans = []
            for i in range(0, len(queue)):
                root = queue.popleft()
                if root.left:
                    levelans.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    levelans.append(root.right.val)
                    queue.append(root.right)
            if levelans:
                ans.append(levelans)
        return ans[::-1]

if __name__ == "__main__":
    root = TreeNode(3)
    root.left, root.right = TreeNode(9), TreeNode(20)
    root.left.right, root.right.left = TreeNode(15), TreeNode(7)
    print(Solution().levelOrderBottom(root))