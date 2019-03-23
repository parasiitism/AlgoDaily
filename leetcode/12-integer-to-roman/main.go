package main

import "fmt"

/*
	1st approach:
	- split cases for 1-3,4,5,6-8,9

	Time    O(n)
	Space   O(n)
	16 ms, faster than 100.00%
*/
func intToRoman(num int) string {
	m := []string{"I", "V", "X", "L", "C", "D", "M"}
	res := ""
	i := 0
	for num > 0 {
		cur := num % 10
		num /= 10
		j := i * 2
		i++

		if cur == 0 {
			continue
		}

		if cur < 5 {
			if cur < 4 {
				res = addMultiple(cur, m[j]) + res // add I,II,II
			} else {
				res = m[j] + m[j+1] + res // add IV
			}
		} else if cur == 5 {
			res = m[j+1] + res // add V
		} else {
			if cur < 9 {
				res = m[j+1] + addMultiple(cur-5, m[j]) + res // add VI,VII,VII
			} else {
				res = m[j] + m[j+2] + res // add IV
			}
		}
	}
	return res
}

func addMultiple(num int, s string) string {
	res := ""
	for i := 0; i < num; i++ {
		res += s
	}
	return res
}

func main() {
	fmt.Println(intToRoman(3999))
}
