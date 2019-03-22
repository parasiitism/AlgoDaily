package main

import "fmt"

/*
	1st approach: 2 pointers
	- if start and end == 0,1,8, left++, right--
	- if start == 6 and end == 9 or vice versa, left++, right--
	- else it is not a strobogrammatic number

	0 ms, faster than 100.00%
*/
func isStrobogrammatic(num string) bool {
	left := 0
	right := len(num) - 1
	for left <= right {
		if (num[left] == '0' && num[right] == '0') ||
			(num[left] == '1' && num[right] == '1') ||
			(num[left] == '8' && num[right] == '8') ||
			(num[left] == '6' && num[right] == '9') ||
			(num[left] == '9' && num[right] == '6') {
			left++
			right--
		} else {
			return false
		}
	}
	return true
}

/*
	1st approach: 2 pointers + hashtable
	- if start and end == 0,1,8, left++, right--
	- if start == 6 and end == 9 or vice versa, left++, right--
	- else it is not a strobogrammatic number

	0 ms, faster than 100.00%
*/
func isStrobogrammatic1(num string) bool {
	m := make(map[byte]byte)
	m['0'] = '0'
	m['1'] = '1'
	m['8'] = '8'
	m['6'] = '9'
	m['9'] = '6'
	left := 0
	right := len(num) - 1
	for left <= right {
		if v, x := m[num[left]]; x && v == num[right] {
			left++
			right--
		} else {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isStrobogrammatic1("919"))
	fmt.Println(isStrobogrammatic1("916"))
	fmt.Println(isStrobogrammatic1("89168"))
}
