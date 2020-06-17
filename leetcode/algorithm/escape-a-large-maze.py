
class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        blocked = set(map(tuple, blocked))
        target = tuple(target)
        source = tuple(source)
        if tuple(target) in blocked:
            return False

        def dfs(start, t, visit):
            if start[0] >= 10 ** 6 or start[0] < 0 or start[1] >= 10 ** 6 or start[1] < 0:
                return False
            if start in blocked:
                return False
            if start in visit:
                return False
            if start == t:
                return True
            if len(visit) > 20000:
                return True
            visit.add(start)
            return dfs((start[0] + 1, start[1]), t, visit) or dfs((start[0], start[1] + 1), t, visit) or dfs((start[0] - 1, start[1]), t,
                                                                                                             visit) or dfs(
                (start[0], start[1] - 1), t, visit)

        return dfs(source, target, set()) and dfs(target, source, set())


s = Solution()
s.isEscapePossible([(10, 11), (11, 10), (9, 10), (10, 9)], (0, 0), (10, 10))
