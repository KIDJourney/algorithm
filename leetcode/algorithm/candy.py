class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = [1 for i in range(len(ratings))]
        right = [1 for i in range(len(ratings))]

        for index, rating in enumerate(ratings[1:], 1):
            if rating > ratings[index-1]:
                left[index] = left[index-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1

        print(left)
        print(right)

        print([max(left[i],right[i]) for i in range(len(ratings))])
        return sum([max(left[i],right[i]) for i in range(len(ratings))])


s = Solution()
s.candy([5,3,1])