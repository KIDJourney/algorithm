class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10 :
            return []

        sub_dir = {}
        ans_sub = []

        str_len = len(s)
        for i in range(str_len-9) :
            sub = s[i:i+10]

            count = sub_dir.get(sub)

            if count == None :
                sub_dir.setdefault(sub,0)
            else :
                sub_dir[sub] += 1
                if sub_dir[sub] == 0 :
                    ans_sub.append(sub)
        return ans_sub