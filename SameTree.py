# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
    	flag = 0
    	if p.val != q.val :
    		return False
    	if p.left != None and q. left != None:
    		return self.isSameTree(p.left,q.left)
    		flag = 1
    	if p.right != None and q.right != None:
    		return self.isSameTree(p.right,q.right)
    		flag = 1
    	if flag == 0 :
    		return False
    	return True