package main

/*
	1st approach: classic bit op
	Time	O(number of bits of num)
	Space	O(1)
	17jan2019
*/
func hammingWeight(num uint32) int {
	result := 0
	x := num
	for x > 0 {
		if x&1 == 1 {
			result++
		}
		x = x >> 1
	}
	return result
}

func main() {

}
