class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        avg_element = target // len(arr)
        g1 = self.guess(arr, avg_element)
        g2 = self.guess(arr, avg_element + 1)

        d1 = self.cal_diff(arr, g1, target)
        d2 = self.cal_diff(arr, g2, target)

        if d1 == d2:
            return min(g1, g2)

        if d1 > d2:
            return g2
        else:
            return g1

    def guess(self, arr, avg):
        diff = 0
        for i in arr:
            if i >= avg:
                continue
            diff += avg - i

        return diff / len(arr) + avg

    def cal_diff(self, arr, value, target):
        ts = 0
        for i in arr:
            if value > i:
                ts += i
            else:
                ts += value

        return abs(target - ts)


s = Solution()
print(s.findBestValue([2, 3, 5], 10))
