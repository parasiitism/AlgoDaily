package main

/*
	questions to ask:
	- are the cost of add, delete, remove the same? yes
	- will there be empty strings? yes

	classic dynamic programming approach
	- https://www.youtube.com/watch?v=We3YDTzNXEk
	- https://www.youtube.com/watch?v=MiqoA-yF-0M
	- https://www.youtube.com/watch?v=ocZMDMZwhCY

	Time    O(word1 * word2)
	Space    O((word1+1) * (word2+1))
	8 ms, faster than 87.31%
*/
func minDistance(word1 string, word2 string) int {
	dp := [][]int{}
	l1 := len(word1)
	l2 := len(word2)
	for i := 0; i < l1+1; i++ {
		temp := []int{}
		for j := 0; j < l2+1; j++ {
			if i == 0 {
				temp = append(temp, j)
			} else if j == 0 {
				temp = append(temp, i)
			} else {
				temp = append(temp, 0)
			}
		}
		dp = append(dp, temp)
	}

	for i := 0; i < l1; i++ {
		for j := 0; j < l2; j++ {
			if word1[i] == word2[j] {
				dp[i+1][j+1] = dp[i][j]
			} else {
				a := dp[i][j]
				b := dp[i][j+1]
				c := dp[i+1][j]
				t := findMin(findMin(a, b), c)
				dp[i+1][j+1] = t + 1
			}
		}
	}
	return dp[l1][l2]
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {

}
