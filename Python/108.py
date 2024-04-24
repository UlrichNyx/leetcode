# 108. Convert Sorted Array to Binary Search Tree
# URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        root = None
        if len(nums) > 0:
            root = TreeNode(nums[len(nums) // 2])
            root.left = self.sortedArrayToBST(nums[:(len(nums) // 2)])
            root.right = self.sortedArrayToBST(nums[(len(nums) // 2) + 1:])
        return root

        