package main

/*
	Questions to ask:
	- charactors in J are distinct?
	- J only consists of alphabets?
	- how big is the input, roughly?
*/

/*
	naive approach: brute force, O(N^2) but O(1) space
*/

/*
	1st approach: hashset
	Time		O(len(J)+len(S))
	Space		O(len(J))
	17jan2019
*/
func numJewelsInStones(J string, S string) int {
	hash := make(map[byte]bool)
	for i := 0; i < len(J); i++ {
		hash[J[i]] = true
	}
	cnt := 0
	for i := 0; i < len(S); i++ {
		if _, x := hash[S[i]]; x {
			cnt++
		}
	}
	return cnt
}

func main() {

}
