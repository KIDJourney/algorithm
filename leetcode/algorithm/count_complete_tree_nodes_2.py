# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.max_h = 0
        self.leaf_cnt = 0
        self.count(root)

        return (2 ** (self.max_h - 1)) - 1 + self.leaf_cnt

    def count(self, root, level=0):
        if not root:
            return
        level += 1
        if level > self.max_h:
            self.max_h = level
            self.leaf_cnt = 0

        if level == self.max_h:
            self.leaf_cnt += 1

        if root.left:
            self.count(root.left, level)

        if root.right:
            self.count(root.right, level)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)

print(s.countNodes(root))
