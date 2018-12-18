package main

import (
	"fmt"
	"math"
)

// 1st attempt
// O(n+m) n: len(list1), m: len(list2)
// beats 93.33%
func findRestaurant(list1 []string, list2 []string) []string {
	hash := make(map[string]int)
	for i := 0; i < len(list1); i++ {
		cur := list1[i]
		hash[cur] = i
	}
	result := []string{}
	lastSum := math.MaxInt64
	for i := 0; i < len(list2); i++ {
		cur := list2[i]
		val, ex := hash[cur]
		if ex {
			if val+i < lastSum {
				result = []string{cur}
				lastSum = val + i
			} else if val+i == lastSum {
				result = append(result, cur)
			}
		}
	}
	return result
}

func main() {
	a := []string{"Shogun", "Tapioca Express", "Burger King", "Piatti"}
	b := []string{"Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun", "Burger King"}
	fmt.Println(findRestaurant(a, b))
}
