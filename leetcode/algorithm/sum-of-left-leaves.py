# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root)
        return self.ans
    def dfs(self, node, is_left=False):
        if not node:
            return 
        if node.left is None and node.right is None and is_left:
            self.ans += node.val
        self.dfs(node.left, is_left=True)
        self.dfs(node.right)
            
        
        
            