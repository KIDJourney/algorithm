class Solution(object):
    mod = 1e9 + 7

    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        one_pos = []
        for idx, i in enumerate(s):
            if i == '1':
                one_pos.append(idx)

        if len(one_pos) == 0:
            return self.combine(len(s) - 1, 2)

        if len(one_pos) % 3 != 0:
            return 0

        print(one_pos)

        parts = len(one_pos) // 3

        pre_zero_nums = one_pos[parts] - one_pos[parts - 1]
        after_zero_nums = one_pos[parts * 2] - one_pos[parts * 2 - 1]

        return int((self.combine(pre_zero_nums, 1) * self.combine(after_zero_nums, 1)) % self.mod)

    def combine(self, a, b):
        up = 1
        down = 1
        for i in range(1, a + 1):
            up = up * i
        for i in range(1, b + 1):
            down = down * i
        for i in range(1, a - b + 1):
            down = down * i

        return int((up // down) % self.mod)


s = Solution()
print(s.numWays('00111'))
print(s.combine(14, 1))
