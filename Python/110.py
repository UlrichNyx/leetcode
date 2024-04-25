# 110. Balanced Binary Tree
# URL: https://leetcode.com/problems/balanced-binary-tree/

import math

class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        return abs(self.findDepth(root.left, 0) - self.findDepth(root.right, 0)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def findDepth(self, root, count):
        if root is None:
            return count
        count += 1
        return max(self.findDepth(root.left, count), self.findDepth(root.right, count))