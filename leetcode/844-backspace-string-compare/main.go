package main

/*
	1st approach: stack

	Time	O(S+T)
	Space	O(S+T)
	0 ms, faster than 100.00%
*/
func backspaceCompare(S string, T string) bool {
	a := ""
	for i := 0; i < len(S); i++ {
		c := string(S[i])
		if c == "#" {
			if len(a) > 0 {
				a = a[:len(a)-1]
			}
		} else {
			a += c
		}
	}
	b := ""
	for i := 0; i < len(T); i++ {
		c := string(T[i])
		if c == "#" {
			if len(b) > 0 {
				b = b[:len(b)-1]
			}
		} else {
			b += c
		}
	}
	return a == b
}

func main() {

}
