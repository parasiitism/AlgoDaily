package main

import (
	"fmt"
)

func isHappy(n int) bool {
	hash := make(map[int]bool)
	temp := n
	for {
		_, ex := hash[temp]
		if ex {
			break
		}
		hash[temp] = true
		arr := unfold(temp)
		newTemp := 0
		for i := 0; i < len(arr); i++ {
			newTemp += arr[i] * arr[i]
		}
		temp = newTemp
	}
	return temp == 1
}

func unfold(n int) []int {
	res := []int{}
	for n > 0 {
		r := n % 10
		res = append(res, r)
		n = n / 10
	}
	return res
}

func main() {
	fmt.Println(isHappy(19))
}
