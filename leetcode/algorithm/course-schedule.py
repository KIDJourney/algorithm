class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        self.global_visit = set()
        self.relation = dict()
        for re in prerequisites:
            self.relation.setdefault(re[1], set())
            self.relation[re[1]].add(re[0])

        for node in self.relation.keys():
            if node in self.global_visit:
                continue
            if self.have_cycle(node, set()):
                return False

        return True
    
    def have_cycle(self, node, visit):
        if node in visit:
            # hava cycle
            return True
        
        if node in self.global_visit:
            # have visited
            return False
        
        for subnode in self.relation.get(node, []):
            nv = set(visit)
            nv.add(node)
            if self.have_cycle(subnode, nv):
                return True
            # subnode not cycle
            self.global_visit.add(subnode)

        return False
            
        
