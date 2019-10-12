class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []
        last_pos = {}
        for idx, s in enumerate(S):
            last_pos[s] = idx

        parts = []

        i = 0
        max_end = -1
        while i < len(S):
            max_end = max(max_end, last_pos[S[i]])
            if max_end == i:
                parts.append(i)
                max_end = i

            i += 1

        ret = [0] + [i + 1 for i in parts]
        new_ret = []
        for idx in range(1, len(ret)):
            new_ret.append(ret[idx] - ret[idx - 1])

        return new_ret


s = Solution()
# S = "ababcbacadefegdehijhklij"
S = ""
# [9,7,8]
result = s.partitionLabels(S)

print(result)
