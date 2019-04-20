package main

/*
	1st approach: 3 passes
	1. check if the result of removing of any character in s equals t
	2. check if the result of removing of any character in t equals s
	3. check if removing any same-positioned character in both s and t which makes them the same

	Time    O(S+T+min(S,T))
	Space   O(1)
	124 ms, faster than 5.18%
*/
func isOneEditDistance(s string, t string) bool {
	if s == t {
		return false
	}
	// check remove s
	for i := 0; i < len(s); i++ {
		x := s[:i] + s[i+1:]
		if x == t {
			return true
		}
	}
	// check remove t
	for i := 0; i < len(t); i++ {
		x := t[:i] + t[i+1:]
		if x == s {
			return true
		}
	}
	// since we now check 'edit', both strings must have length
	if len(s) != len(t) {
		return false
	}
	// check remove s and remove t
	for i := 0; i < len(s); i++ {
		x := s[:i] + s[i+1:]
		y := t[:i] + t[i+1:]
		if x == y {
			return true
		}
	}
	return false
}

/*
	2nd approach: check substrings
	- when we encounter different characters at the same index, compare the remaining substrings

	There're 3 possibilities to satisfy the question:
	1) Replace 1 char:
 	  s: a B c
 	  t: a D c
  2) Delete 1 char from s:
	  s: a D  b c
	  t: a    b c
  3) Delete 1 char from t
	  s: a   b c
	  t: a D b c

	Time		O(min(S,T))
	Space		O(1)
	0 ms, faster than 100.00%
*/
func isOneEditDistance1(s string, t string) bool {
	for i := 0; i < min(len(s), len(t)); i++ {
		if s[i] != t[i] {
			if len(s) == len(t) {
				// s has the same length as t, so the only possibility is replacing one char in s and t
				return s[i+1:] == t[i+1:]
			} else if len(s) > len(t) {
				// s is longer than t, so the only possibility is deleting one char from s
				return s[i+1:] == t[i:]
			} else {
				// t is longer than s, so the only possibility is deleting one char from t
				return s[i:] == t[i+1:]
			}
		}
	}
	if len(s)-len(t) == 1 || len(t)-len(s) == 1 {
		return true
	}
	return false
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {

}
