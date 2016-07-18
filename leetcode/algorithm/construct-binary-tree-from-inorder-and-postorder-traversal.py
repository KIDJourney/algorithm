# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build_tree(left, right):
            if left < right:
                root = TreeNode(postorder.pop())
                root_pos = inorder.index(root.val)
                root.right = build_tree(root_pos + 1, right)
                root.left = build_tree(left, root_pos)
                return root

        return build_tree(0, len(inorder))



s = Solution()
tree = s.buildTree([4, 2, 5, 1, 6, 7, 3, 8], [4, 5, 2, 6, 7, 8, 3, 1])