# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.trave(root)

        return self.ans
        

    def trave(self, node):
        if not node :
            return 
        
        self.trave(node.left)
        self.trave(node.right)
        self.ans.append(node.val)


