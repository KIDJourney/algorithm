class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tire = Tire()
        for num in nums:
            binary = bin(num)[2:]
            binary = (32 - len(binary)) * '0' + binary
            tire.insert(binary)
        ret = 0
        for num in nums:
            tmp_max = 0
            tmp_node = tire.root
            for i in list(range(32))[::-1]:
                tmp_max *= 2
                tmp = (num >> i) & 1
                if 1 - tmp in tmp_node:
                    tmp_max += 1
                    tmp_node = tmp_node[1-tmp]
                else :
                    tmp_node = tmp_node[tmp]
            ret = max(tmp_max, ret)
        return ret
                



class Tire:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        tmp = self.root
        for ch in word:
            tmp.setdefault(int(ch), {})
            tmp = tmp[int(ch)]

s = Solution()
s.findMaximumXOR([])