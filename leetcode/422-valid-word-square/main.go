package main

import "fmt"

/*
	1st approach:
	- the main idea is to check if words[i][j] == words[j][i]

	be careful of the corner cases:

	e.g.1
	"ball",
	"areae",
	"read",
	"lady",

	e.g.2
	"ball",
	"areae",
	"read",
	"lady",
	"e",

	Time	O()

	4 ms, faster than 100.00%
*/
func validWordSquare(words []string) bool {
	for i := 0; i < len(words); i++ {
		for j := 0; j < len(words[i]); j++ {
			if j >= len(words) {
				return false
			} else if i >= len(words[j]) {
				return false
			} else if words[i][j] != words[j][i] {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Println(validWordSquare([]string{
		"abcd",
		"bnrt",
		"crmy",
		"dtye",
	}))

	fmt.Println(validWordSquare([]string{
		"abcd",
		"bnrt",
		"crm",
		"dt",
	}))

	fmt.Println(validWordSquare([]string{
		"ball",
		"area",
		"read",
		"lady",
	}))

	fmt.Println(validWordSquare([]string{
		"ball",
		"areae",
		"read",
		"lady",
	}))

	fmt.Println(validWordSquare([]string{
		"ball",
		"areae",
		"read",
		"lady",
		"e",
	}))

	fmt.Println(validWordSquare([]string{}))

	fmt.Println(validWordSquare([]string{
		"e",
	}))

	fmt.Println(validWordSquare([]string{
		"ball",
	}))
}
