import random


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_link(number):
    if number == 0:
        return Node(0)
    pre = None
    head = None
    while number:
        head = Node(number % 10)
        number = number // 10
        head.next = pre
        pre = head
    return head


def get_link_number(head):
    ret = ''
    while head:
        ret += str(head.val)
        head = head.next
    return int(ret)


def combine_two_link(l1, l2):
    ret = Node(0)
    tmph = ret
    while l1 and l2:
        if l1.val >= l2.val:
            tmph.next = l2
            l2 = l2.next
        else:
            tmph.next = l1
            l1 = l1.next
        tmph = tmph.next
    if l1:
        tmph.next = l1
    if l2:
        tmph.next = l2
    return ret.next


def reverse_link(l):
    pre = None
    now = l
    nex = None
    while now:
        nex = now.next
        now.next = pre
        pre = now
        now = nex
    return pre


def add_two_link(l1, l2):
    l1 = reverse_link(l1)
    l2 = reverse_link(l2)
    head = Node(0)
    pre = head
    carry = 0
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
     
        tmp_sum = v1 + v2 + carry
        carry = tmp_sum // 10

        tmp_node = Node(tmp_sum % 10)
        pre.next = tmp_node

        pre = tmp_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    if carry:
        pre.next = Node(carry)

    return reverse_link(head.next)


for a, b in [[1,2], [9999,1],[1,9999],[11111111111,222222222222]]:
    ans = a + b
    print(a, b)
    print("True: ", a + b)

    a = build_link(a)
    b = build_link(b)

    res = get_link_number(add_two_link(a, b))
    print("Ans: ", res)
    assert ans == res
