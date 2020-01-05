# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.min_string = None

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.min_string = None
        self.dfs(root, "")

        return self.min_string or ''

    def dfs(self, node, value):
        if not node:
            if self.min_string is None:
                self.min_string = value
            else:
                self.min_string = min(self.min_string, value)
            return

        self.dfs(node.left, self.to_chr(node.val) + value)
        self.dfs(node.right, self.to_chr(node.val) + value)

    @staticmethod
    def to_chr(i):
        return chr(ord('a') + i)
