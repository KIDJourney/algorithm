class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for n in nums:
            t = t ^ n

        return t


if __name__ == "__main__":
    s = Solution()
    print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
