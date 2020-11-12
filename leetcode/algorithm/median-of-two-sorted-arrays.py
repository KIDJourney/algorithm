class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        mid_idx = length // 2
        i = 0
        j = 0
        while mid_idx:
            if i >= len(nums1):
                break
            if j >= len(nums2):
                break
            if nums1[i] > nums2[j]:
                i += 1
                mid_idx -= 1
            else:
                j += 1
                mid_idx -= 1

        while mid_idx:
            if i < len(nums1):
                i += mid_idx
            