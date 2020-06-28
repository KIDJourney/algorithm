import heapq


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        items = sorted(zip(Capital, Profits))
        idx = 0
        heap = []
        for _ in range(k):
            while idx < len(items) and items[idx][0] <= W:
                heapq.heappush(heap, (-items[idx][1], items[idx][0]))
                idx += 1
            if heap:
                W -= heapq.heappop(heap)[0]

        return W


s = Solution()
print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
