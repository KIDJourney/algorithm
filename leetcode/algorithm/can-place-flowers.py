class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for idx, i in enumerate(flowerbed):
            if i == 0:
                flag = True
                if idx - 1 >= 0:
                    if flowerbed[idx - 1] != 0:
                        flag = False

                if idx + 1 < len(flowerbed):
                    if flowerbed[idx + 1] != 0:
                        flag = False

                if flag:
                    flowerbed[idx] = 1
                    n -= 1

        return n <= 0
