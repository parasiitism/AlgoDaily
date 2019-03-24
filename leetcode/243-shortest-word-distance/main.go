package main

/*
	questions to ask:
  - will word1 == word2?
  - will either word1, word2 be in the list always?
*/

/*
	1st approach: 2pointers

	Time    O(n)
	Space   O(1)
*/
func shortestDistance(words []string, word1 string, word2 string) int {
	p1 := -1
	p2 := -1
	res := len(words)
	for i := 0; i < len(words); i++ {
		word := words[i]
		if word == word1 {
			p1 = i
		}
		if word == word2 {
			p2 = i
		}
		diff := abs(p1 - p2)
		if p1 != -1 && p2 != -1 && diff < res {
			res = diff
		}
	}
	return res
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {

}
