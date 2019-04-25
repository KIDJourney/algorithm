class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        s = set()
        if A == B:
            for i in A:
                if i in s:
                    return True
                s.add(i)
            return False

        diff = []
        for idx in range(len(A)):
            if A[idx] != B[idx]:
                diff.append((A[idx], B[idx]))

        if len(diff) != 2:
            return False

        if diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]:
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.buddyStrings('ab', 'ab'))
