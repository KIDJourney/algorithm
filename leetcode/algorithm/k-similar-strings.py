class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        def swap(s, i, j):
            j, i = max(i, j), min(i, j)
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        ret = 0
        if A == B:
            return ret

        pos_mapping = {}
        for idx, c in enumerate(B):
            pos_mapping.setdefault(c, [])
            pos_mapping[c].append(idx)

        visited = {(A, 0)}
        queue = [(A, 0)]

        while queue:
            k = 0
            new_queue = []

            for job, offset in queue:
                for idx in range(offset, len(job)):
                    pass


s = Solution()
print(s.kSimilarity('abcbca', 'ababcc'))
