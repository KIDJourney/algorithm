class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        one_pos = []
        for idx, s in enumerate(seats):
            if s == 1:
                one_pos.append(s)

        ret = 0

        for idx in range(1, len(one_pos)):
            ret = min


s = Solution()
print(s.maxDistToClosest([1, 0, 0, 0, 0, 1, 0, 1]))
