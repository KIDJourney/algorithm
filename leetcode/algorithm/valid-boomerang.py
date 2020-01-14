class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points[0] == points[1] and points[1] == points[2]:
            return False


