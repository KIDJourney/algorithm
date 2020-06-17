class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        if not light:
            return 0
        ans = 0
        max_l = light[0]
        max_c = 0

        if max_l == 1:
            ans += 1

        for l in light[1:]:
            if l > max_l:
                max_l = l

            max_c += 1

            if max_l - 1 == max_c:
                ans += 1

        return ans
