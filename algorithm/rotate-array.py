class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
