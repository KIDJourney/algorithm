class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums :
            return []
        if len(nums) < 2 :
            return [str(nums[0])]
        anslist = []
        start = 0
        end = 0
        for i in range(len(nums))[1:] :
            if nums[i] - nums[i-1] == 1:
                end = i
            else :
                if start == end :
                    anslist.append(str(nums[start]))
                else :
                    anslist.append("%d->%d" %(nums[start] , nums[end]))
                start = i
                end = i
        if start == end :
            anslist.append(str(nums[start]))
        else :
            anslist.append("%d->%d" %(nums[start] , nums[end]))
        return anslist
