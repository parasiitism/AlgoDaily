package main

/*
	1st approach:
	- 2 index pointers: 1 for first non-zero number, 1 for last zeo
	- swap the non-zero number with the zero
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
