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
<<<<<<< HEAD
    def isSameTree(self, p, q) :
        if p is None or q is None :
            return p == q
        if p.val != q.val  :
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
=======
    def isSameTree(self, p, q):
    	
>>>>>>> 7ae4dfdd2b8f2c6e29d95f3488c54890b4a0fe17
