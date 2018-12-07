class DataNode(object):
    def __init__(self, front, tail, key, value):
        self.front = front
        self.tail = tail
        self.key = key
        self.value = value


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.front_node = None
        self.tail_node = None

        self.d = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1

        node = self.d[key]

        front, tail = node.front, node.tail

        if front:
            front.tail = tail
        if tail:
            tail.front = front

        ofront = self.tail_node

        node.front = None
        ofront.front = node
        node.tail = ofront
        self.front_node = node

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = DataNode(None, None, key, value)

        if self.front_node is None:
            self.front_node = node
        if self.tail_node is None:
            self.tail_node = node

        ofront = self.tail_node

        node.front = None
        ofront.front = node
        node.tail = ofront
        self.front_node = node
        self.d[key] = node

        if len(self.d) > self.capacity:
            self.tail_node = self.tail_node.front
            del self.d[key]


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
