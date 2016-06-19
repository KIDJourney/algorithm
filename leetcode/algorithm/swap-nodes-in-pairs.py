class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = pointer = ListNode(0)
        new_head.next = head

        while pointer.next is not None and pointer.next.next is not None:
            temp_node = pointer.next.next
            pointer.next.next = temp_node.next
            temp_node.next = pointer.next
            pointer.next = temp_node
            pointer = pointer.next.next

        return new_head.next


nodes = ListNode(1)
nodes.next = ListNode(2)
nodes.next.next = ListNode(3)
nodes.next.next.next = ListNode(4)

s = Solution()
s.swapPairs(nodes)

