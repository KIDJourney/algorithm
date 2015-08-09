# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headB or not headA :
            return None 
        ans = None
        a = headA
        b = headB
        while a or b :
            if not a :
                a = headB
            if not b :
                b = headA
            if a==b and not ans :
                ans = a
            a , b = a.next , b.next
        return ans