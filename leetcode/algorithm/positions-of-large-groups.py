class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        if not S:
            return []
        w = ""
        s = 0
        c = 0
        for idx, char in enumerate(S):
            if char != w:
                if c >= 3:
                    ret.append([s, s + c - 1])
                s = idx
                w = char
                c = 1
            else:
                c += 1

        if c >= 3:
            ret.append((s, s + c - 1))
        return ret


s = Solution()
print(s.largeGroupPositions("abbxxxxzzy"))
print(s.largeGroupPositions("abcdddeeeeaabbbcd"))
