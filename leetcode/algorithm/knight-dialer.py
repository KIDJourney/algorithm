m = 10 ** 9 + 7


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0:
            return 0

        self.cache = {}
        self.target_map = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9],
            5: [],
            6: [1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        st = 0
        for i in range(10):
            st += self.dfs(i, N)
        return st % m

    def dfs(self, pos, n):
        if n == 1:
            return len(self.target_map[pos])

        if (pos, n) in self.cache:
            return self.cache[(pos, n)]

        tsum = 0
        for next_pos in self.target_map[pos]:
            cnt = self.dfs(next_pos, n - 1)
            self.cache[(next_pos, n - 1)] = cnt
            tsum += cnt % m

        return tsum % m


s = Solution()
for i in range(1, 4):
    print(s.knightDialer(i))
