import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.l = []
        self.len = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.map[val] = self.len
        self.len += 1
        self.l.append(val)

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.map:
            return False

        pos = self.map[val]
        last_v = self.l[self.len - 1]
        del self.map[val]
        self.l[pos], self.l[self.len - 1] = self.l[self.len - 1], self.l[pos]
        self.map[last_v] = pos
        self.len -= 1

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.len)
        return self.l[idx]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
param_1 = obj.insert(4)
param_1 = obj.insert(5)
param_2 = obj.remove(3)
for i in range(10):
    print(obj.getRandom())
