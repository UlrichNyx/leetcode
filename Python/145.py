# 145. Binary Tree Postorder Traversal
# URL: https://leetcode.com/problems/binary-tree-postorder-traversal/


class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )
