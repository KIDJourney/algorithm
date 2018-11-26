# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        ret = []
        while queue:
            nq = []
            tsum = 0
            tcount = 0
            for node in queue:
                if not node:
                    continue
                else:
                    tsum += node.val
                    tcount += 1
                    if node.left:
                        nq.append(node.left)
                    if node.right:
                        nq.append(node.right)
            ret.append(tsum / float(tcount))
            queue = nq

        return ret
