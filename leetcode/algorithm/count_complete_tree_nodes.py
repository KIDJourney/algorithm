# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        cnt = 0
        q = [root]
        while q:
            nq = []
            for n in q:
                if not n:
                    continue
                cnt += 1
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            q = nq

        return cnt
