# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None :
            return False    
        return self.dfs(root,0,sum)

    def dfs(self,root,tnum,sum) :
        if root is None :
            return False
        if root.left is None and root.right is None :
            return tnum + root.val == sum
        else :
            return self.dfs(root.left , tnum+root.val , sum) or self.dfs(root.right , tnum+root.val , sum)
