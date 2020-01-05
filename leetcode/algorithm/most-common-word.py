from string import ascii_letters


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = ''.join([i.lower() for i in paragraph if i in set(ascii_letters + ' ')])
        banned = set()

        counter = {}
        for word in paragraph.split():
            counter.setdefault(word, 0)
            counter[word] += 1

        keys = set(counter.keys())


