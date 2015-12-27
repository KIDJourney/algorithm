import functools
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitmap , length = [self.bitop(word) for word in words] , [len(word) for word in words]

        maxvalue = 0

        for i in range(len(bitmap)):
            for j in range(i + 1 , len(bitmap)):
                if bitmap[i] &  bitmap[j] == 0:
                    maxvalue = max (length[i] * length[j] , maxvalue)

        return maxvalue

    def bitop(self,word):
        return functools.reduce(lambda x , y : x | (1<<(y-ord('a'))) , map(ord , word) , 0)