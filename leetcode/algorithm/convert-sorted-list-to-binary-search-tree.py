# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

    def build_tree(self, node):
        if not node:
            return
        one_step_node = node
        two_step_node = node

        while two_step_node is not None and two_step_node.next is not None:
            one_step_node, two_step_node = one_step_node.next, two_step_node.next.next

        new_node = TreeNode(one_step_node)
