class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        bit_p = {}
        new_arr = []
        for s in arr:
            v = 0
            for c in s:
                new_v = v | (1 << (ord(c) - ord('a')))
                if new_v == v:
                    v = -1
                    break
                else:
                    v = new_v
            if v == -1:
                continue
            bit_p[s] = v
            new_arr.append(s)

        arr = new_arr
        if not arr:
            return 0

        self.bit_p = bit_p
        self.arr = arr
        self.max_len = len(arr[0])

        self.dfs(0, "", 0)
        return self.max_len

    def dfs(self, start, now, now_bit):
        for i in range(start, len(self.arr)):
            if now_bit & self.bit_p[self.arr[i]] == 0:
                new_str = now + self.arr[i]
                self.max_len = max(self.max_len, len(new_str))
                new_bit = now_bit | self.bit_p[self.arr[i]]
                self.dfs(i + 1, new_str, new_bit)


s = Solution()
print(s.maxLength(["yy", "bkhwmpbiisbldzknpm"]))
