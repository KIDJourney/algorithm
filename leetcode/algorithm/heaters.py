class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        index = 0
        r = 0
        for house in sorted(houses):
            # brilliant
            while house > sum(heaters[index:index+2]) // 2:
                index += 1
            r = max(r, abs(heaters[index] - house))

        return r

s = Solution()
print(s.findRadius([1,2,3],[2]))