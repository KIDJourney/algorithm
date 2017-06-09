# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        l1 = self.getLength(headA)
        l2 = self.getLength(headB)

        dis = abs(l1-l2)

        longer = headA if l1 > l2 else headB
        shorter = headB if l1 < l2 else headA
        
        p1, p2 = longer, shorter

        while dis:
            p1 = p1.next
            dis -= 1
        
        while p1 and p2 :
            if p1 == p2 :
                return p1
            p1 = p1.next
            p2 = p2.next

        return None
        
    def getLength(self, l):
        count = 0
        while l:
            l = l.next
            count += 1
        return count

