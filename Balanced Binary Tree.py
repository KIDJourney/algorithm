# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __intit__(self) :
        self.falg = 1
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        self.dfs(root)
        if self.flag != 1 :
            return False 
        else :
            return True

    def dfs(self , root) :
        if self.falg == 0:
            return -1
        if root is None :
            return 0

        ll = self.dfs(root.left) +1
        lr = self.dfs(root.rgiht) +1

        if (ll-lr)*(ll-lr) >= 1 :
            self.falg = 0

        if ll > lr :
            return ll 
        else :
            return lr

