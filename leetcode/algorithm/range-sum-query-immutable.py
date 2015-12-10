class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums

        for i in range(1,len(self.nums)) :
            self.nums[i] = self.nums[i-1] + self.nums[i]
    

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0 :
            return self.nums[j]        
        else :
            return self.nums[j] - self.nums[i-1]


