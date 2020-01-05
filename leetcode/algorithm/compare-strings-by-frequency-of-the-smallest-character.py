from collections import Counter


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        query = [self.cal(i) for i in queries]
        words = sorted([self.cal(i) for i in words])
        print(query)
        print(words)

        ret = []
        for q in query:
            cnt = 0
            for idx, wc in enumerate(words):
                if wc > q:
                    cnt = len(words) - idx
                    break
            ret.append(cnt)

        return ret

    @staticmethod
    def cal(word):
        cnt = Counter(word)
        return cnt[min(cnt.keys())]

    @staticmethod
    def lower_bound(l, target):
        s, e = 0, len(l) - 1
        while s <= e:
            mid = (s + e) // 2
            if l[mid] >= target:
                e = mid - 1
            else:
                s = mid + 1

        return 0


s = Solution()
print(s.numSmallerByFrequency(["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"],
                              ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]))
