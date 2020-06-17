# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.find_leaf(root1) == self.find_leaf(root2)

    def find_leaf(self, node):
        if not node:
            return []

        if not node.left and not node.right:
            return [node.val]

        return self.find_leaf(node.left) + self.find_leaf(node.right)
