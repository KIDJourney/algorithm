/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	if len(s) <= 1 {
		return 1
	}
	s, e := 0, 0
	ans := 0
	meet := map[string]bool{}
	for true {
		if e < s {
			e = s
		}
		nextc := s[e+1]
		if _, ok := meet[nextc]; ok {
			meet[s] = false
			s += 1
		}

	}

}

// @lc code=end

