class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        one_cnt = 0
        zero_cnt = 0
        for s in students:
            if s == 1:
                one_cnt += 1
            else:
                zero_cnt += 1

        sand_one = 0
        sand_zero = 0
        idx = 0
        for s in sandwiches:
            if s == 1:
                sand_one += 1
            else:
                sand_zero += 1

            if sand_one > one_cnt:
                break
            if sand_zero > zero_cnt:
                break

            idx += 1

        return len(students) - idx
