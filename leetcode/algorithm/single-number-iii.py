class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor = 0
        for i in nums :
            xor ^= i
        xor = xor & (xor -1) ^ xor          # get the different i bit  , e.g. 00001000
        a = b = 0
        for i in nums :
            if i & xor :          # if the ith bit equal xor 
                a = a ^ i
            else :
                b = b ^ i

        return [a,b]

job = Solution()
print(job.singleNumber([1,1,3,3,2,5]))