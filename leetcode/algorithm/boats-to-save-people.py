class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        n = 0
        i, j = 0, len(people) - 1
        while i <= j:
            n += 1
            if i == j:
                i += 1
                continue
            if people[i] + people[j] > limit:
                if people[i] > people[j]:
                    i += 1
                else:
                    j -= 1

            else:
                i += 1
                j -= 1

        return n


s = Solution()
print(s.numRescueBoats([3, 5, 3, 4], 5))
