class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nmap = {}
        for num in nums:
            nmap[num] = True

        max_len = 0

        for idx, key in enumerate(nmap):
            if key - 1 in nmap:
                continue
            tn = 0
            while key in nmap:
                tn += 1
                max_len = max(max_len, tn)
                key += 1

        return max_len
