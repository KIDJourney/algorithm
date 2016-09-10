class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0 :
                break
            j = i+1
            k = len(nums)-1
            while j < k:
                t_sums = nums[i] + nums[j] + nums[k]
                if t_sums == 0:
                    ans.add(nums[i],nums[j],nums[k])
                if t_sums < 0 :
                    j += 1
                if t_sums > 0:
                    k += 1
        while nums[i] != nums[i-1]: i+= 1
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))