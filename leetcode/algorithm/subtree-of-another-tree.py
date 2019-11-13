# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s is None and t is None:
            return True

        if s and t:
            if s.val == t.val:
                return self.isSubtree(s.left, t.left) or self.isSubtree(s.right, t.right)
            else:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        if s is not None and t is None:
            return True

        return False
