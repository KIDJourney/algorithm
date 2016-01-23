class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split();
        if len(str) != len(pattern):
            return False
        pattern2str = {}
        str2pattern = {}
        for index , value in enumerate(pattern):
            w2p = str2pattern.setdefault(str[index],value)
            p2w = pattern2str.setdefault(value,str[index])
            if w2p != value or p2w != str[index]:
                return False
        return True