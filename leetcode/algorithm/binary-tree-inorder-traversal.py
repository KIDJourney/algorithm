# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.ans

    def inorder(self,root):
        if not root :
            return 
        if root.left :
            self.inorder(root.left)
        self.ans.append(root.val);
        if root.right:
            self.inorder(root.right)
        