class Solution(object):
    def complexNumberMultiply(self, x, y):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b = self.split_complex(x)
        c,d = self.split_complex(y)
        ans_r = a*c - b*d
        comp = b*c + a*d

        return '{}+{}i'.format(ans_r, comp)


    @staticmethod
    def split_complex(strnum):
        strnum = strnum.replace('i','')
        real, comp = map(int, strnum.split('+'))
        return real, comp

s = Solution()
print(s.complexNumberMultiply("1+-1i","1+-1i"))