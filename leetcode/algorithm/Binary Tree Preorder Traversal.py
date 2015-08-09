# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root :
            return []
        self.ans = []
        self.preorder(root)
        return self.ans


    def preorder(self,node):
        self.ans.append(node.val)
        if node.left :
            self.preorder(node.left)
        if node.right :
            self.preorder(node.right)
