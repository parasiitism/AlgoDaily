package main

/*
	1st approach:
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

func main() {

}
