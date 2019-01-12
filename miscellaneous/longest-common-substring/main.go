package main

import "fmt"

/*
	questions to ask interviewer
	- lower case & upper case?
	- if there are more than one longest substrings which have the same length?
*/

/*
	naive approach: brute force
	4 pointers: 2 for finding the starting positions, 2 for extending the substring
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

/*
	i can do it with a trie, but the time complexity is the same. and the implementation is painful
	so i am not gonna implement
*/

/*
	2nd approach: learned from others https://www.youtube.com/watch?v=aVFWW3pBQFo
	- dynamic programming
	- construct a 2D array which cache the common substrings on previous iteration
	- see ./idea.jpeg
	Time	O(n^2)
	Space	O(n^2)
	The one who came up with this method is genius
*/
func lcs(s1 string, s2 string) string {
	dp := [][]string{}
	for i := 0; i < len(s1); i++ {
		temp := []string{}
		for j := 0; j < len(s2); j++ {
			temp = append(temp, "")
		}
		dp = append(dp, temp)
	}
	result := ""
	for i := 0; i < len(s1); i++ {
		for j := 0; j < len(s2); j++ {
			if s1[i] != s2[j] {
				continue
			}
			upperRight := ""
			if i > 0 && j > 0 {
				upperRight = dp[i-1][j-1]
			}
			dp[i][j] = upperRight + string(s1[i])
			if len(dp[i][j]) > len(result) {
				result = dp[i][j]
			}
		}
	}
	return result
}

func main() {
	a := "cdabxyzccznmotuv"
	b := "aabzdazccznmvvtcdabx"
	fmt.Println(longestCommonSubstring(a, b))
	fmt.Println(lcs(a, b))
}
