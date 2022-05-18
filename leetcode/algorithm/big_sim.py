def big_sum(values, steps):
    score = 0
    last_choice = 0

    def get_sum(l, r):
        return sum(values[l:r])

    left, right = 0, len(values)
    for step in steps:
        left_start, left_end = left, step
        right_start, right_end = step + 1, right

        lv = get_sum(left_start, left_end)
        rv = get_sum(right_start, right_end)

        if lv > rv:
            left, right = right_start, right_end
            last_choice = 0
            score += rv
        if lv < rv:
            left, right = left_start, left_end
            last_choice = 1
            score += lv
        if lv == rv:
            if last_choice == 0:
                left, right = right_start, right_end
                score += rv
            else:
                left, right = left_start, left_end
                score += lv
            last_choice = 1 - last_choice

        if 