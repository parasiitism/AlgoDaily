package main

func containsDuplicate(nums []int) bool {
	hash := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		if hash[nums[i]] {
			return true
		}
		hash[nums[i]] = true
	}
	return false
}

func main() {

}
