class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum([ i < j for i , j in enumerate(sorted(citations,reverse = True))])