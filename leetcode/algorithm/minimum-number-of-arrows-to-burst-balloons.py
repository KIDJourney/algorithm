class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1]) 
        count, end = 0, -float('inf')
        for p in points:
            if p[0] > end:
                count += 1
                end = p[1]
        return count    

s = Solution()
print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))