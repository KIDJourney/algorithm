class DuLNode(object):
    def __init__(self, k, v, pre, nxt):
        self.pre = pre
        self.nxt = nxt
        self.key = k
        self.value = v


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = DuLNode(None, 'head', None, None)
        self.tail = DuLNode(None, 'tail', None, None)

        self.head.nxt = self.tail
        self.tail.pre = self.head

        self.map = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.show_link()
        if key not in self.map:
            return -1

        node = self.map[key]
        self.move_to_first(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.show_link()
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.move_to_first(node)
            return

        if len(self.map) == self.capacity:
            self.remove_tail()

        new_node = DuLNode(key, value, None, None)
        self.move_to_first(new_node)

        self.map[key] = new_node

    def move_to_first(self, node):
        if node is None:
            return

        node_pre = node.pre
        node_nxt = node.nxt

        if node_pre is not None:
            node_pre.nxt = node_nxt
        if node_nxt is not None:
            node_nxt.pre = node_pre

        head_nxt = self.head.nxt

        self.head.nxt = node
        node.pre = self.head
        node.nxt = head_nxt
        head_nxt.pre = node

    def remove_tail(self):
        tail_pre = self.tail.pre
        tail_pre_pre = tail_pre.pre

        if tail_pre_pre is None:
            return

        tail_pre_pre.nxt = self.tail
        self.tail.pre = tail_pre_pre

        # print('delete map key=%s', tail_pre.key)
        del self.map[tail_pre.key]

    def show_link(self):
        return
        now = self.head
        while now is not None:
            print('now=%s, pre=%s, next=%s', now.pre.value if now.pre else None, now.value, now.nxt.value if now.nxt else None)
            now = now.nxt

    # Your LRUCache object will be instantiated and called as such:


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
