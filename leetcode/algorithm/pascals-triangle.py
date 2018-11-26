#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\pascals-triangle.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-14
# class Solution:
#     # @return a list of lists of integers
#     def generate(self, numRows):
#         if numRows == 0:
#             return []
#         self.anslist = []
#         for i in range(numRows):
#             templist = []
#             for j in range(i + 1):
#                 templist.append(self.select(i, j))
#             self.anslist.append(templist)
#         return self.anslist
#
#     def select(self, base, num):
#         if num == 0:
#             return 1
#         mom = 1
#         kid = 1
#         for i in range(base + 1)[-num:]:
#             kid *= i
#         for i in range(num + 1)[1:]:
#             mom *= i
#         return kid / mom


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows == 0:
            return ret
        for rownum in range(1, numRows + 1):
            row = []
            for col in range(1, rownum + 1):
                if col == 1:
                    row.append(1)
                    continue
                if col == rownum:
                    row.append(1)
                    continue

                row.append(ret[rownum - 2][col - 1] + ret[rownum - 2][col - 2])

            ret.append(row)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.generate(10))
