# 144. Binary Tree Preorder Traversal
# URL: https://leetcode.com/problems/binary-tree-preorder-traversal/


class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )
