class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        numdir = {}
        for i in num :
            if numdir.has_key(i) :
                numdir[i]+=1
            else :
                numdir[i] = 1
        return sorted(numdir.iteritems() , key = lambda x : x[1] , reverse = True)[0][0]

# job = Solution()
# print job.majorityElement([3,3,4])