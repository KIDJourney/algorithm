# Input: ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# Round 1: You could get 5 points. The sum is: 5.
# Round 2: You could get -2 points. The sum is: 3.
# Round 3: You could get 4 points. The sum is: 7.
# Operation 1: The round 3's data is invalid. The sum is: 3.
# Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
# Round 5: You could get 9 points. The sum is: 8.
# Round 6: You could get -4 + 9 = 5 points. The sum is 13.
# Round 7: You could get 9 + 5 = 14 points. The sum is 27.

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        round = []
        for op in ops:
            if op not in {"C", "D", "+"}:
                round.append(int(op))
            if op == "C":
                round.pop()
            if op == "D":
                round.append(round[-1] * 2)
            if op == "+":
                round.append(round[-1] + round[-2])

        return sum(round)


s = Solution()
print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
