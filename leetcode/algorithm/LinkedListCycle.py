# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        newhead = ListNode(0)
        newhead.next = head
        a = newhead
        b = newhead
        while b.next and b.next.next :
            a = a.next
            b = b.next.next
            if a == b :
                return True
        return False

# method 2

# class Solution:
#     # @param head, a ListNode
#     # @return a boolean
#     def hasCycle(self, head):
#         try :
#             a = head
#             b = head.next.next

#             while a!=b :
#                 a = a.next
#                 b = b.next.next
#             return True
#         except :
#             return False