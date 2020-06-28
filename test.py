class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            print(s, e, mid)
            t = nums[mid]
            if t == target:
                return mid
            if t > target:
                e = mid - 1
            elif t < target:
                s = mid + 1

        return -1


s = Solution()
print(s.search([-1, 0, 5], 5))
