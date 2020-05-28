class Solution(object):
    # num = num[:idx] + num[sidx] + num[idx + 1: sidx] + num[idx] + num[sidx + 1:]

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        for idx in range(len(num)):
            idx_v = int(num[idx])
            m, midx = idx_v, idx
            for sidx in range(len(num) - 1, idx, -1):
                sidx_v = int(num[sidx])
                if m < sidx_v:
                    m, midx = sidx_v, sidx

            if idx != midx:
                num = num[:idx] + num[midx] + num[idx + 1: midx] + num[idx] + num[midx + 1:]
                return num

        return int(num)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSwap(2736))
    print(s.maximumSwap(9973))
