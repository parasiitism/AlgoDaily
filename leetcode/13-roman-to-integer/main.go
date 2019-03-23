package main

/*
	1st approach: use a var for previous symbol

	Time    O(n)
	Space   O(1)
	20 ms, faster than 63.93%
*/
func romanToInt(s string) int {
	indeces := make(map[byte]int)
	indeces['I'] = 0
	indeces['V'] = 1
	indeces['X'] = 2
	indeces['L'] = 3
	indeces['C'] = 4
	indeces['D'] = 5
	indeces['M'] = 6

	m := make(map[byte]int)
	m['I'] = 1
	m['V'] = 5
	m['X'] = 10
	m['L'] = 50
	m['C'] = 100
	m['D'] = 500
	m['M'] = 1000

	res := 0
	prev := byte('0')

	for i := 0; i < len(s); i++ {
		c := s[i]
		if prev == '0' {
			prev = c
		} else if indeces[c] <= indeces[prev] {
			res += m[prev]
			prev = c
		} else {
			val := m[c] - m[prev]
			res += val
			prev = byte('0')
		}
	}

	if prev != byte('0') {
		res += m[prev]
	}

	return res
}

func main() {

}
