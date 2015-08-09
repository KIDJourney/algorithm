# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ans = 0
    def maxDepth(self, root):
    	self.dfs(root,0)
    	return self.ans
    def dfs(self,root,step):
		if root == None:
			if step > self.ans:
				self.ans = step
			return
		self.dfs(root.left,step+1)
		self.dfs(root.right,step+1)

#Just a easy def
