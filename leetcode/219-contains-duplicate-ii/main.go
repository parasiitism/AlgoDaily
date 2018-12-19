package main

import "fmt"

// this question is kinda tricky
// since the question says "at most k", it means the range can be less than k
// herefore we actually just need to store the previous index of duplicate charactors
// instead of the indexes of all duplicate charactors in the hashtbale
// O(n)
// beats 87.34%
func containsNearbyDuplicate(nums []int, k int) bool {
	hash := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if v, ex := hash[nums[i]]; !ex {
			hash[nums[i]] = i
		} else {
			// we are doing it in one pass, so i must be larger than any values(indexes) in the hashtable
			if i-v <= k {
				return true
			}
			hash[nums[i]] = i
		}
	}
	return false
}

func main() {
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 1, 2, 3}, 2))
	fmt.Println(containsNearbyDuplicate([]int{1, 2, 3, 1, 2, 3, 1}, 6))
}
