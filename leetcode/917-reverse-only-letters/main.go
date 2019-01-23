package main

import "fmt"

/*
	1st approach
	- 2 pointers only point to alphabet, assign the char to the correct position
	TIme		O(n)
	Space		O(n)
	0ms beats 100%
	21jan2019
*/
func reverseOnlyLetters(S string) string {
	clone := []byte(S)
	i := len(S) - 1
	j := 0
	for i >= 0 {
		if (S[i] >= 65 && S[i] <= 90) || (S[i] >= 97 && S[i] <= 122) {
			if (S[j] >= 65 && S[j] <= 90) || (S[j] >= 97 && S[j] <= 122) {
				clone[j] = S[i]
				i--
				j++
			} else {
				j++
			}
		} else {
			i--
		}
	}
	return string(clone)
}

func main() {
	a := []byte{'b', 'a'}
	b := string(a)
	fmt.Println(b)
	fmt.Println(reverseOnlyLetters(""))
	fmt.Println(reverseOnlyLetters(" "))
	fmt.Println(reverseOnlyLetters("+-"))
	fmt.Println(reverseOnlyLetters("ab-cd"))
	fmt.Println(reverseOnlyLetters("a-bC-dEf-ghIj"))
	fmt.Println(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
}
