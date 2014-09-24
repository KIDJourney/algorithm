class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	return	reduce(lambda x,y : x^y , A)

#This problem is solved by using bit manipulation   	
#When same nums xor we will get 0
#When a num xor 0 we will get origin num
#It's very smart to use this way
#I have learn a lot