package main

/*
	naive approach
	1. for each num, look for forward to find the arithemetic boundary
	2. calculate the count of the arithemetic intermediate array
	Time    O(n^2)
	Space   O(1)
	not gonna implement
*/

/*
	1st appraoch
	- math, use n*(n+1)/2 to calculate the combination count instead of doing brute force
	Time    O(n)
	Space   O(1)
	20ms beats 100%
	31jan2019
*/
func numberOfArithmeticSlices(A []int) int {
	if len(A) < 3 {
		return 0
	}
	diff := A[1] - A[0]
	res := 0
	start := 0
	for i := 1; i < len(A); i++ {
		if A[i]-A[i-1] == diff {
			if i+1 == len(A) {
				res += calCnt(start, i)
			}
			continue
		}
		res += calCnt(start, i-1)
		// be careful: set the next start point from the previous item
		// take this case into consideration [1, 2, 3, 8, 13]
		start = i - 1
		diff = A[i] - A[i-1]
	}
	return res
}

func calCnt(start, i int) int {
	n := i - start + 1
	if n >= 3 {
		cnt := n - 2
		return cnt * (cnt + 1) / 2
	}
	return 0
}

func main() {

}
