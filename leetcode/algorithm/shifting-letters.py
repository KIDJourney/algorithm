class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        base = ord('a')
        if not shifts:
            return S

        all_shift = sum(shifts)
        offset = []
        for i in range(len(shifts)):
            offset.append(all_shift % 26)
            all_shift -= shifts[i]

        new_str = []
        for idx in range(len(S)):
            if idx > len(offset):
                new_str.append(S[idx])
            else:
                new_chr = chr((ord(S[idx]) - base + offset[idx]) % 26 + base)
                new_str.append(new_chr)

        return ''.join(new_str)


s = Solution()
print(s.shiftingLetters('abc', [3, 5, 9]))
