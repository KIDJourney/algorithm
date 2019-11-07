class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = {}
        sorted_n1 = sorted(nums1)[::-1]

        for n2 in nums2:
            while sorted_n1 and n2 > sorted_n1[-1]:
                n1 = sorted_n1.pop()
                ret.setdefault(n1, n2)

        return [ret.get(i, -1) for i in nums1]


s = Solution()
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
