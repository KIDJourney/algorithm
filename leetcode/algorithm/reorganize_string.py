class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        counter = {}
        for c in S:
            counter.setdefault(c, 0)
            counter[c] += 1

        ret = ''
        counter = list(sorted(counter.items(), key=lambda x: -x[1]))
        while len(counter) > 1:
            top_2 = counter[:2]
            bp, sp = top_2[0][1], top_2[1][1]
            if top_2[0][1] > top_2[1][1]:
                pass
            else:
                bp, sp = sp, bp
