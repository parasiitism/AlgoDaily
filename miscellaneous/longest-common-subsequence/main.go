package main

import (
	"fmt"
	"strconv"
)

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
func lcs_dp(s1 string, s2 string) string {
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

/*
	https://www.youtube.com/watch?v=sSno9rV8Rhg
	recursive
*/
func lcs_recursive(s1 string, s2 string) string {
	return helper(s1, s2, 0, 0)
}
func helper(s1 string, s2 string, i int, j int) string {
	if i < 0 || i+1 > len(s1) || j < 0 || j+1 > len(s2) {
		return ""
	} else if s1[i] == s2[j] {
		return string(s1[i]) + helper(s1, s2, i+1, j+1)
	} else {
		a := helper(s1, s2, i+1, j)
		b := helper(s1, s2, i, j+1)
		if len(a) > len(b) {
			return a
		}
		return b
	}
}

func lcs_recursive_mem(s1 string, s2 string) string {
	cache := make(map[string]string)
	return helper_mem(s1, s2, 0, 0, cache)
}
func helper_mem(s1 string, s2 string, i int, j int, cache map[string]string) string {
	key := strconv.Itoa(i) + "," + strconv.Itoa(j)
	if v, x := cache[key]; x {
		return v
	}
	if i < 0 || i+1 > len(s1) || j < 0 || j+1 > len(s2) {
		return ""
	} else if s1[i] == s2[j] {
		temp := string(s1[i]) + helper_mem(s1, s2, i+1, j+1, cache)
		cache[key] = temp
		return temp
	} else {
		a := helper_mem(s1, s2, i+1, j, cache)
		b := helper_mem(s1, s2, i, j+1, cache)
		if len(a) > len(b) {
			cache[key] = a
			return a
		}
		cache[key] = b
		return b
	}
}

func main() {
	fmt.Println(lcs_dp("BATD", "ABACD"))
	fmt.Println(lcs_dp("XMJYAUZ", "MZJAWXU"))
	fmt.Println(lcs_dp("XMJYAUZMJ", "MZJAWXUM"))
	fmt.Println(lcs_dp("ABCDEFGHIJKLM", "CFKABEFJMABC"))

	fmt.Println(lcs_recursive("BATD", "ABACD"))
	fmt.Println(lcs_recursive("XMJYAUZ", "MZJAWXU"))
	fmt.Println(lcs_recursive("XMJYAUZMJ", "MZJAWXUM"))
	fmt.Println(lcs_recursive("ABCDEFGHIJKLM", "CFKABEFJMABC"))

	fmt.Println(lcs_recursive_mem("BATD", "ABACD"))
	fmt.Println(lcs_recursive_mem("XMJYAUZ", "MZJAWXU"))
	fmt.Println(lcs_recursive_mem("XMJYAUZMJ", "MZJAWXUM"))
	fmt.Println(lcs_recursive_mem("ABCDEFGHIJKLM", "CFKABEFJMABC"))
}
