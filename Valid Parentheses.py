class Solution:
    # @return a boolean
    def isValid(self, s):
        pair = (('(',')'),('[',']'),('{','}'))
        list = []
        for i in s :
            if i in ('(','[','{') :
                list.append(i)
            else :
                if len(list) == 0:
                    return False
                p = list.pop()
                for j in pair :
                    if p == j[0] and i == j[1] :
                        break
                else :
                    return False
                
        if len(list) != 0 :
            return False
        else :
            return True

