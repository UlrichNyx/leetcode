# 111. Balanced Binary Tree
# URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        return self.countHeight(root, 0)
    def countHeight(self, root, count):
        count += 1
        if not root is None and root.left is None and root.right is None:
            return count
        elif root.left is None:
            return self.countHeight(root.right, count)
        elif root.right is None:
            return self.countHeight(root.left, count)
        return min(self.countHeight(root.left, count), self.countHeight(root.right, count))