class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import Counter
        secret_count = dict(Counter(secret))
        guess_count = dict(Counter(guess))

        print(secret_count)
        print(guess_count)

        A = sum(secret[i] == guess[i] for i , _ in enumerate(secret))
        B = sum([min(secret_count[i] , guess_count[i]) for i in secret_count.keys() if i in guess_count.keys()]) - A

        return "{0}A{1}B".format(A,B)

job = Solution()
print(job.getHint('1','0'))