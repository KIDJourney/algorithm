# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head :
            return None 
        temp = head 
        while (temp.next) :
            if temp.val == temp.next.val :
                temp.next = temp.next.next
                continue
            else :
                temp = temp.next
        return head