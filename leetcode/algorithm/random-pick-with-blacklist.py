import random
class Solution(object):
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.bl = set(blacklist)
        self.ava = [i for i in range(N) if i not in self.bl]

    def pick(self):
        """
        :rtype: int
        """
        idx = random.randint(0, len(self.ava)-1)
        return self.ava[idx]


s = Solution(1, [])
for i in range(10):
    print(s.pick())

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
