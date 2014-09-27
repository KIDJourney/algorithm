# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	self.iddir = {}
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    	if id(head) in self.iddir.keys():
    		self.iddir[id(head)] += 1
    		if self.iddir[id(head)] > 1 :
    			return False
    	else :
    		self.iddir[id(head)] = 1

    	if head.next is None :
    		return True
    	else :
    		return self.hasCycle(head.next)