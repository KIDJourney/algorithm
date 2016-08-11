class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        lists = []
        node = head
        if not head :
            return 

        while node:
            lists.append(node)
            node = node.next

        s, e = 0, len(lists) - 1

        now = lists[s]
        pos = 0

        while s <= e:
            if pos == 0:
                now.next = lists[e]
                s += 1
                now = lists[e]
            else :
                now.next = lists[s]
                e -= 1
                now = lists[s]

            pos = 1 - pos 

        now.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
s = Solution()
s.reorderList(head)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)