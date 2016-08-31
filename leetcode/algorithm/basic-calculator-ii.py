action_map = {
    '+': lambda x,y:x+y,
    '-': lambda x,y:x-y,
    '*': lambda x,y:x*y,
    '/': lambda x,y:x//y
}
privilege = ['*','/']

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_next_number(pos):
            number = ''
            while pos < len(s) and s[pos] not in action_map.keys():
                number += s[pos]
                pos += 1
            return (int(number), pos)
        s = s.replace(' ','')
        pos = 0
        stack = []
        while pos < len(s):
            if s[pos] in action_map.keys():
                if s[pos] in privilege:
                    symbol = s[pos]
                    a = stack.pop()
                    b, new_pos = get_next_number(pos+1)
                    pos = new_pos
                    stack.append(action_map[symbol](a,b))
                else :
                    stack.append(s[pos])
                    pos += 1
            else:
                number, new_pos = get_next_number(pos)
                stack.append(number)
                pos = new_pos
        action = action_map.get('+')
        ans = 0
        for i in stack:
            if i in action_map:
                action = action_map[i]
            else :
                ans = action(ans,i)

        return ans

s = Solution()
print(s.calculate('1-123*5'))