# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.ans = []
        self.delete_value = set(to_delete)

    def del_node(self, head, parent):
        if head.val in self.delete_value:
            if parent.left:
                self.ans.append(parent.left)
            if parent.right:
                self.ans.append(parent.right)
            parent.left, parent.right = None, None
