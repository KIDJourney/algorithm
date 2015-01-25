# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    iddir = {}
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head) :
        if head is None :
            return False
        else :
            if id(head) in self.iddir.key() :
                self.iddir[id(head)] += 1
                if self.iddir[id(head)] >= 1 :
                    return True
            else :
                self.iddir[id(head)] = 1
                return self.hasCycle(head.next)