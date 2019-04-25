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

        for i in range(len(A)):
            if A[i] == B[i]:
                continue

            pos_list = pos_mapping.get(A[i])
            swap_pos = 0
            for pos in pos_list:
                if pos > i:
                    if A[i] == A[pos]:
                        continue
                    swap_pos = pos
                    break

            A = swap(A, i, swap_pos)
            ret += 1

        return ret


s = Solution()
print(s.kSimilarity('abcbca', 'ababcc'))
