class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        i1 = 0
        i2 = 0

        ans = []

        while i1 < nums1_len and i2 < nums2_len:
            if nums1[i1] != nums2[i2]:
                if nums1[i1] > nums2[i2]:
                    i2 += 1
                else :
                    i1 += 1
            else :
                ans.append(nums1[i1])
                i1 += 1
                i2 += 1

        return ans

s = Solution()
print(s.intersect([1,2,2,3],[2,2]))
