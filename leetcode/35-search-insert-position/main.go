package main

func searchInsert(nums []int, target int) int {
	min := 0
	max := len(nums)
	for min < max {
		mean := (min + max) / 2
		if target <= nums[mean] {
			max = mean
		} else {
			min = mean + 1
		}
	}
	return min
}

func main() {

}
