class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nbin = map(int, bin(n)[3:])
        if nbin.count(1) == len(nbin):
            return len(nbin) + 3

        ret = 0
        e = len(nbin) - 1

        while e >= 0:
            if nbin[e] == 0:
                ret += 1
                e -= 1
                continue

            cnt_1 = 0
            s = e
            while s >= 0:
                if nbin[s] == 1:
                    cnt_1 += 1
                    s -= 1
                else:
                    s -= 1
                    break

            if cnt_1 >= 3:
                ret += 1 + cnt_1 + 2
            else:
                ret += 2 * cnt_1

            e = s

        return ret


s = Solution()
print(s.integerReplacement(3))
print(s.integerReplacement(8))
print(s.integerReplacement(7))
print(s.integerReplacement(31))
print(s.integerReplacement(23))
print(s.integerReplacement(65535))
