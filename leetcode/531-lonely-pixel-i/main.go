package main

/*
	1st approach: hashtable
	1. for row, if there are 'B', calculate the number of 'B' for those columns
	2. if that row only has 1 'B', check if there is only one 'B' on that column
	3. be careful of 'one column checking'

	Time		O(m*n*n)
	Space		O(n)
	4 ms, faster than 100.00%
*/
func findLonelyPixel(picture [][]byte) int {
	if len(picture) == 0 || len(picture[0]) == 0 {
		return 0
	}
	cache := make(map[int]int)
	res := 0
	for i := 0; i < len(picture); i++ {
		found := -1
		for j := 0; j < len(picture[0]); j++ {
			if picture[i][j] == 'B' {
				calColCache(picture, j, cache)
				if found == -1 {
					found = j
				} else {
					// be careful, once there are more than 1, dont let any one set it again
					found = -2
				}
			}
		}
		if found > -1 {
			if v, x := cache[found]; x && v == 1 {
				res++
			}
		}
	}
	return res
}

func calColCache(picture [][]byte, col int, cache map[int]int) {
	if _, x := cache[col]; x {
		return
	}
	count := 0
	for i := 0; i < len(picture); i++ {
		if picture[i][col] == 'B' {
			count++
		}
	}
	cache[col] = count
}

func main() {

}
