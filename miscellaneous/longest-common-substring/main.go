package main

import "fmt"

/*
	naive approach: brute force
	Time	O(n^3)
	Space	O(1)
*/
func longestCommonSubstring(s1 string, s2 string) string {
	result := ""
	for i := 0; i < len(s1); i++ {
		for j := 0; j < len(s2); j++ {
			if s1[i] == s2[j] {
				temp := string(s1[i])
				for k, l := i+1, j+1; k < len(s1); k, l = k+1, l+1 {
					if l >= len(s2) || s1[k] != s2[l] {
						break
					}
					temp += string(s1[k])
				}
				if len(temp) > len(result) {
					result = temp
				}
			}
		}
	}
	return result
}

func main() {
	a := "cdabxyzccznmotuv"
	b := "aabzdazccznmvvtcdabx"
	fmt.Println(longestCommonSubstring(a, b))
}
