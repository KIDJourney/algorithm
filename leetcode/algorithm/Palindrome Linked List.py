# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        pre = None
        slow = fast = head
        while fast and fast.next :
            fast = fast.next.next
            pre  , pre.next , slow = slow , pre , slow.next
        if fast :
            slow = slow.next
        while pre and slow :
            if pre.val != slow.val :
                return False
            pre = pre.next
            slow = slow.next
        return True
