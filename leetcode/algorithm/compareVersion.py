class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        longer_one = max(len(version1), len(version2))

        version1 += [0] * (longer_one - len(version1))
        version2 += [0] * (longer_one - len(version2))
        for index in range(min(len(version1), len(version2))):
            if version1[index] > version2[index]:
                return 1
            if version1[index] < version2[index]:
                return -1
        
        return 0

s= Solution()
print(s.compareVersion('1','1.1'))