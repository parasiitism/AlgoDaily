package main

/*
	1st approach: better brute force using a hash table

	Time	O(n^2)
	Space	O(n)
	4 ms, faster than 100.00%
*/
func nextGreaterElement(findNums []int, nums []int) []int {
	res := []int{}
	m := make(map[int]int)
	for i, num := range nums {
		m[num] = i
	}
	for _, num := range findNums {
		i := m[num]
		found := -1
		for j := i; j < len(nums); j++ {
			if nums[j] > num {
				found = nums[j]
				break
			}
		}
		res = append(res, found)
	}
	return res
}

func main() {

}
