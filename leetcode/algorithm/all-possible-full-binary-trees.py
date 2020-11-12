from copy import deepcopy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        super(Solution, self).__init__()
        self.cache = {}

    def allPossibleFBT(self, n):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        n -= 1
        if n in self.cache:
            return self.cache[n]

        if n == 0:
            return [TreeNode(0)]

        ret = []
        for l in range(1, n, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(n - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret.append(root)

        self.cache[n] = ret
        return ret
