# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, current_value, depth):
            if not node:
                return depth

            nd = depth
            if node.val == current_value:
                nd += 1
            else:
                nd = 0

            return max(dfs(node.left, node.val, nd), dfs(node.right, node.val, nd))

        return dfs(root, None, 0)


"""           5
             / \
            4   5
           / \   \
          1   1   5"""
