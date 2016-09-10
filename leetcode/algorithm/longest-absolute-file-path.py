strings = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.split('\n')

        pre_level = -1
        level_length = 0
        parent_length = 0
        longest_length = 0        
        length = 0
        
        for line in lines :
            level = line.count('\t')
            if level == pre_level + 1:
                parent_length = len(line.strip())
                level_length += parent_length
                level += 1
                continue
            elif level == pre_level:
                
                



s = Solution()
assert s.lengthLongestPath(strings) == 32