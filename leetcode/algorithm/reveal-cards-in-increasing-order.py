class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        order = get_order(len(deck))
        deck = sorted(deck)

        ret = [0 for i in range(len(deck))]

        for idx, o in enumerate(order):
            ret[o - 1] = deck[idx]

        return ret


def get_order(n, l=None):
    if l is None:
        l = range(1, n + 1)
    out = []
    while l:
        out.append(l[0])
        l = l[1:]

        if len(l) > 1:
            l = l[1:] + [l[0]]

    return out


print(get_order(10))

# s = Solution()
# print(s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
