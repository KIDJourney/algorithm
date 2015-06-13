# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
        print (ans)
        head = ListNode(0)
        s = head
        while ans :
            s.next = ListNode(ans%10)
            s = s.next
            ans = int(ans/10)
        return head.next


def showList(l1) :
    if l1.next :
        showList(l1.next)
    print(l1.val)

l1 = ListNode(1)
l1.next = ListNode(2)

l2 = ListNode(2)
l2.next = ListNode(5)

job = Solution()
showList(job.addTwoNumbers(l1,l2))