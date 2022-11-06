#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        return self.easy(nums1, nums2)

    def easy(self, nums1, nums2):
        result = []
        idx1, idx2 = 0, 0
        while True:
            if idx1 == len(nums1) and idx2 == (len(nums2)):
                break

            if idx1 == len(nums1):
                result.append(nums2[idx2])
                idx2 += 1
                continue
            if idx2 == len(nums2):
                result.append(nums1[idx1])
                idx1 += 1
                continue

            if nums1[idx1] > nums2[idx2]:
                result.append(nums2[idx2])
                idx2 += 1
            else:
                result.append(nums1[idx1])
                idx1 += 1
        mid = len(result) // 2
        if len(result) % 2 == 0:
            return (result[mid] + result[mid-1]) / 2.0
        else:
            return (result[mid])


# @lc code=end
