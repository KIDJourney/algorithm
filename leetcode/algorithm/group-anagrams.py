class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = {}
        for s in strs:
            ts = ''.join(sorted(s))
            ht.setdefault(ts, [])
            ht[ts].append(s)

        return list(ht.values())


class SolutionV2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ht = {}
        for s in strs:
            sh = self.strhash(s)
            ht.setdefault(sh, [])
            ht[sh].append(s)

        return list(ht.values())

    def strhash(self, s):
        counter = [0 for i in range(26)]
        for c in s:
            counter[ord(c) - ord('a')] += 1

        return ''.join(map(str, counter))


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
