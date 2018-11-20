class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        changed = True
        while True:
            if not changed:
                if senate[0] == 'R':
                    return "Radiant"
                else:
                    return "Dire"

            changed = False
            ns = []
            rc = 0
            dc = 0
            for s in senate:
                if s == 'R':
                    if dc > 0:
                        dc -= 1
                        changed = True
                    else:
                        ns.append(s)
                        rc += 1
                else:
                    if rc > 0:
                        rc -= 1
                        changed = True
                    else:
                        ns.append(s)
                        dc += 1

            senate = ''.join(ns)
            print(senate)
            

                

if __name__ == "__main__":
    s = Solution()
    print(s.predictPartyVictory("RD"))
    print(s.predictPartyVictory("RDD"))
    print(s.predictPartyVictory("DDRRRR"))