class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = 0
        for i in A:
            if i % 2 == 0:
                even_sum += i

        ret = []

        for q in queries:
            v, idx = q[0], q[1]

            before_val = A[idx]
            A[idx] += v

            if before_val % 2 == 0:
                even_sum -= before_val
            if A[idx] % 2 == 0:
                even_sum += A[idx]

            ret.append(even_sum)

        return ret


s = Solution()
print(s.sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
