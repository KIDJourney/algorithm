# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        self.ret = None
        self.min_score = None

        self.dfs(root, 0, 0, "")
        return self.ret[::-1]

    def dfs(self, node, score, deep, seq=""):
        new_score = score + ((node.val + 1) * (27 ** deep))
        new_seq = seq + chr(ord('a') + node.val)
        if not node.left and not node.right:
            if self.ret is None or new_score < self.min_score:
                self.min_score = new_score
                self.ret = new_seq
                return

        if node.left:
            self.dfs(node.left, new_score, deep + 1, new_seq)
        if node.right:
            self.dfs(node.right, new_score, deep + 1, new_seq)
