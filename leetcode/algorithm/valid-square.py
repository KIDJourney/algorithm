class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dis = []
        pl = [p1, p2, p3, p4]
        for i in range(len(pl)):
            for j in range(i + 1, len(pl)):
                dis.append((pl[i][0] - pl[j][0]) ** 2 + (pl[i][1] - pl[j][1]) ** 2)

        cnt = {}
        for i in dis:
            cnt.setdefault(i, 0)
            cnt[i] += 1

        for k in cnt:
            if cnt[k] == 4:
                return True

        return False


s = Solution()
p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]
print(s.validSquare(p1, p2, p3, p4))
