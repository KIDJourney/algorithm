# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n :
            return None

        if isBadVersion(1):
            return 1

        s = 1
        e = n

        while (s <= e) :
            half = int((s+e)/2)

            if isBadVersion(half) and not isBadVersion(half-1):
                return half

            if isBadVersion(half-1):                
                e = half
            else :
                s = half + 1