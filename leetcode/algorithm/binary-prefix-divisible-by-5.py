class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        tmp_sub = 0
        ret = []
        for i in A:
            tmp_sub = tmp_sub * 2 + i
            if tmp_sub % 5 == 0:
                ret.append(True)
            else:
                ret.append(False)

        return ret
