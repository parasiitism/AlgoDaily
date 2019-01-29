package main

/*
	1st approach
	- +-x, +-y
	4ms beats 100%
	29jan2019
*/
func judgeCircle(moves string) bool {
	x := 0
	y := 0
	for i := 0; i < len(moves); i++ {
		if moves[i] == 'U' {
			y++
		} else if moves[i] == 'D' {
			y--
		} else if moves[i] == 'R' {
			x++
		} else if moves[i] == 'L' {
			x--
		}
	}
	return x == 0 && y == 0
}

/*
	1st approach
	- hashtable
	20ms beats 0%
	29jan2019
*/
func judgeCircle1(moves string) bool {
	ht := make(map[byte]int)
	ht['U'] = 0
	ht['D'] = 0
	ht['R'] = 0
	ht['L'] = 0
	for i := 0; i < len(moves); i++ {
		ht[moves[i]]++
	}
	return ht['U'] == ht['D'] && ht['R'] == ht['L']
}

func main() {

}
