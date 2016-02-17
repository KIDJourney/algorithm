# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return None
        oddStart = head
        evenStart = head.next
        oddNode = oddStart
        evenNode = head.next
        while evenNode is not None and evenNode.next is not None:
            oddNode.next = evenNode.next
            oddNode = oddNode.next
            evenNode.next = oddNode.next
            evenNode = evenNode.next
        oddNode.next = evenStart
        return head
