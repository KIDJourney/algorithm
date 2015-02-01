class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        posa = m-1
        posb = n-1 
        for i in range(0,m+n)[::-1] :
            if posa >= 0 and posb >= 0 and A[posa] > B[posb] :
                A[i] = A[posa]
                posa -= 1
            elif (posb >= 0) :
                A[i] = B[posb]
                posb -= 1
