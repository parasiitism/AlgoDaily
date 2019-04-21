package main

/*
	1st approach:
	- 2 index pointers: slow pointer points to the first zero, fast pointer is for iteration
	- swap the non-zero number with the zero

	Time		O(n)
	Space		O(1)
	64 ms, faster than 89.29%
*/
func moveZeroes(nums []int) {
	idx0 := -1
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[idx0+1], nums[i] = nums[i], nums[idx0+1]
			idx0++
		}
	}
}

func main() {

}
