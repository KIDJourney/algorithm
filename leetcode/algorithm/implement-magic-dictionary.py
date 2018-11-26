from string import ascii_lowercase


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, d):
        """
        Build a dictionary through a list of words
        :type d: List[str]
        :rtype: void
        """
        self.d = set(d)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for idx in range(len(word)):
            for c in [i for i in ascii_lowercase if i != word[idx]]:
                if word[:idx] + c + word[idx + 1:] in self.d:
                    return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
print(obj.search('heleo'))
