class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        tmap = {}
        reverse_map = {}
        for tpair in trust:
            tmap.setdefault(tpair[1], [])
            tmap[tpair[1]].append(tpair[0])

            reverse_map.setdefault(tpair[0], [])
            reverse_map[tpair[0]].append(tpair[1])

        for i in range(1, N + 1):
            if len(tmap.get(i, [])) == N - 1 and len(reverse_map.get(i, [])) == 0:
                return i

        return -1


s = Solution()
print(s.findJudge(1, []))
