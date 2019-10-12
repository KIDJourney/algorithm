class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        edge = {}
        for node, to_nodes in enumerate(graph):
            edge.setdefault(node, set())
            for to_node in to_nodes:
                edge[node].add(to_node)

        visit = {}
        color = []

        queue = list(edge.keys())
        c = 0
        while queue:
            node = queue.pop()
            if node in visit:
                if


s = Solution()
print(s.isBipartite([[3, 4, 6], [3, 6], [3, 6], [0, 1, 2, 5], [0, 7, 8], [3], [0, 1, 2, 7], [4, 6], [4], []]))
print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
# 3   4
# 6
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(s.isBipartite([[1], [0, 3], [3], [1, 2]]))
