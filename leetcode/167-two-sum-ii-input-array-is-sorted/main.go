package main

import (
	"fmt"
	"strconv"
)

func twoSum(numbers []int, target int) []int {
	var hashtable = make(map[int]string)
	for i := 0; i < len(numbers); i++ {
		offset := target - numbers[i]
		if hashtable[numbers[i]] != "" {
			idx, _ := strconv.Atoi(hashtable[numbers[i]])
			return []int{idx + 1, i + 1}
		} else {
			hashtable[offset] = strconv.Itoa(i)
		}
	}
	return []int{-1, -1}
}

func main() {
	ans := twoSum([]int{2, 9}, 11)
	fmt.Println(ans)
}
