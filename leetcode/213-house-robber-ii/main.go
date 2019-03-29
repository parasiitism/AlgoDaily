package main

/*
	1st approach: reuse leetcode 213
	- since adjacent means only the i-1 and i+1, problem becomes to rob either
		ouse[0]-House[n-2] or House[1]-House[n-1], depending on which choice offers more money

	Time		O(2n)
	Space		O(1)
	0 ms, faster than 100.00%
*/
func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	if len(nums) == 2 {
		return max(nums[0], nums[1])
	}
	a := notCicular(nums[:len(nums)-1])
	b := notCicular(nums[1:])
	return max(a, b)
}

func notCicular(nums []int) int {
	prevprev := 0
	prev := 0
	for i := 0; i < len(nums); i++ {
		cur := nums[i]
		temp := max(prevprev+cur, prev)
		prevprev = prev
		prev = temp
	}
	return prev
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {

}
