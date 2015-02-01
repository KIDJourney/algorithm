    class Solution:
        # @param version1, a string
        # @param version2, a string
        # @return an integer
        def compareVersion(self, version1, version2):
            version1 = map(int,version1.split('.'))
            version2 = map(int,version2.split('.'))
            lengh = 0
            lv1 = len(version1)
            lv2 = len(version2)
            if lv1 > lv2 :
                version2 += [0] * (lv1 - lv2)
                lengh = lv1
            else :
                version1 += [0] * (lv2 - lv1)
                lengh = lv2

            for i in range(lengh) :
                if version1[i] > version2[i] :
                    return 1 
                if version2[i] > version1[i] :
                    return -1
                if version1[i] == version2[i] :
                    continue
            return 0
