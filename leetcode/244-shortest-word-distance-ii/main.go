package main

type WordDistance struct {
	Words []string
	M     map[string]int
}

func Constructor(words []string) WordDistance {
	return WordDistance{words, make(map[string]int)}
}

func (this *WordDistance) Shortest(word1 string, word2 string) int {
	key1 := word1 + "<>" + word2
	if v, x := this.M[key1]; x {
		return v
	}
	key2 := word2 + "<>" + word1
	if v, x := this.M[key2]; x {
		return v
	}
	p1 := -1
	p2 := -1
	res := len(this.Words)
	for i := 0; i < len(this.Words); i++ {
		word := this.Words[i]
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
	key := word1 + "<>" + word2
	this.M[key] = res
	return res
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

/**
* Your WordDistance object will be instantiated and called as such:
* obj := Constructor(words);
* param_1 := obj.Shortest(word1,word2);
 */

func main() {

}
