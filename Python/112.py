# 112. Path Sum
# URL: https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        return self.truePathSum(root, targetSum)
    
    def truePathSum(self, root, targetSum):
        if not root is None and root.left is None:
            return self.truePathSum(root.right, targetSum - root.val)
        elif not root is None and root.right is None:
            return self.truePathSum(root.left, targetSum - root.val)
        elif root is None:
            return targetSum == 0
        return self.truePathSum(root.left, targetSum - root.val) or self.truePathSum(root.right, targetSum - root.val)