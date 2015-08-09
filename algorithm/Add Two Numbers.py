# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        ans = 0
        pos = 1
        while l1 and l2 :
            ans += (l1.val + l2.val) * pos
            pos *= 10
            l1 = l1.next
            l2 = l2.next
        while l1 :
            ans += (l1.val) * pos
            pos *= 10
            l1 = l1.next
        while l2 :
            ans += (l2.val) * pos
            pos *= 10
            l2 = l2.next
        print (ans)
        head = ListNode(0)
        s = head
        if not ans :
            return head
        while ans :
            s.next = ListNode(ans%10)
            s = s.next
            ans = int(ans/10)
        return head.next