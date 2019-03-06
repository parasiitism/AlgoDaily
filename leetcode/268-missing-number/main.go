package main

/*
	1st approach: math
	- n(n+1)/2-sum

	Time	O(n)
	Space	O(1)

	16 ms, faster than 100.00%
*/
func missingNumber(nums []int) int {
	end := len(nums) + 1
	supposedSum := end * len(nums) / 2
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return supposedSum - sum
}

/*
	2nd approach: bucket ordering
	- put the items into buckets
	- traverse the buckets and return i if the i-th bucket is empty

	Time	O(2n)
	Space	O(n)

	16 ms, faster than 100.00%
*/
func missingNumber1(nums []int) int {
	buckets := make([]int, len(nums)+1)
	for _, num := range nums {
		buckets[num]++
	}
	for i, b := range buckets {
		if b == 0 {
			return i
		}
	}
	return -1
}

func main() {

}
