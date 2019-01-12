package main

import "fmt"

// honestly, i dont even know how to brute force it...

/*
	1st approach:
	- dynamic programming similar to longest common substring
	- construct a 2D array which cache the common substrings on previous iteration
	- see ./idea.jpeg
	Time	O(n^2)
	Space	O(n^2)
	The one who came up with this method is genius
*/
func lcs(s1 string, s2 string) string {
	// construct a matrix
	dp := [][]string{}
	for i := 0; i < len(s1); i++ {
		temp := []string{}
		for j := 0; j < len(s2); j++ {
			temp = append(temp, "")
		}
		dp = append(dp, temp)
	}
	// iterate the arrays and append the result
	for i := 0; i < len(s1); i++ {
		for j := 0; j < len(s2); j++ {
			up := ""
			if i > 0 {
				up = dp[i-1][j]
			}
			if s1[i] == s2[j] {
				dp[i][j] = up + string(s1[i])
			} else {
				right := ""
				if j > 0 {
					right = dp[i][j-1]
				}
				// save the largest value amongst up and right
				// prefer to save right
				if len(up) > len(right) {
					dp[i][j] = up
				} else {
					dp[i][j] = right
				}
			}
		}
	}
	return dp[len(s1)-1][len(s2)-1]
}

func main() {
	fmt.Println(lcs("BATD", "ABACD"))
	fmt.Println(lcs("XMJYAUZ", "MZJAWXU"))
	fmt.Println(lcs("XMJYAUZMJ", "MZJAWXUM"))
	fmt.Println(lcs("ABCDEFGHIJKLM", "CFKABEFJMABC"))
}
