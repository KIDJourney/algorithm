class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word = set('balloon')
        counter = {}
        for w in word:
            counter[w] = 0

        for t in text:
            if t in word:
                counter.setdefault(t, 0)
                counter[t] += 1

        for c in 'lo':
            if c in counter:
                counter[c] /= 2

        return min(counter.values())
