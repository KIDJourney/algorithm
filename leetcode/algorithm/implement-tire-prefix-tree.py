class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}

    def get(self, key):
        return self.child.get(key)

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            node = node.child.setdefault(char, TrieNode())
        node.child['end'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            node = node.get(char)
            if not node:
                return False
        if 'end' in node.child:
            return True
        else :
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            node = node.get(char)
            if not node:
                return False
        return True