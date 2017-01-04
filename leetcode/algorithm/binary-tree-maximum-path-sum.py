# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = -99999999
        self.maxSubPath(root)
        return self.maxValue

    def maxSubPath(self,node):
        if node is None :
            return 0
        left =  max(0, self.maxSubPath(node.left))
        right = max(0, self.maxSubPath(node.right))
        self.maxValue = max(self.maxValue, left+right+node.val)

        return max(left,right) + node.val

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

s = Solution()
print(s.maxPathSum(root))