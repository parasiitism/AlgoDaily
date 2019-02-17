package main

import "fmt"

/*
	corner test:
	- 1 to many / many to many e.g. {good, great} , {good, nice}, {good, exellent}

	learned from others:
	- use hashtable to save one pair e.g. a#b
	- when we iterate the words, search a#b and b#a

	Time	O(n)
	Space	O(n)
	4ms beats 100%
*/
func areSentencesSimilar(words1 []string, words2 []string, pairs [][]string) bool {
	if len(words1) != len(words2) {
		return false
	}
	m := make(map[string]bool)
	for _, pair := range pairs {
		m[pair[0]+"|"+pair[1]] = true
	}
	for i := 0; i < len(words1); i++ {
		a := words1[i]
		b := words2[i]
		if a == b {
			continue
		}
		key1 := a + "|" + b
		key2 := b + "|" + a
		found1 := true
		if _, x := m[key1]; !x {
			found1 = false
		}
		found2 := true
		if _, x := m[key2]; !x {
			found2 = false
		}
		if found1 == false && found2 == false {
			return false
		}
	}
	return true
}

func main() {
	a := []string{"great", "acting", "skills"}
	b := []string{"fine", "drama", "talent"}
	p := [][]string{{"great", "good"}, {"fine", "good"}, {"acting", "drama"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilar(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama", "talent"}
	p = [][]string{{"great", "good"}, {"fine", "great"}, {"acting", "drama"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilar(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama", "talent"}
	p = [][]string{{"fine", "great"}, {"fine", "good"}, {"acting", "drama"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilar(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama", "talent"}
	p = [][]string{{"fine", "good"}, {"fine", "great"}, {"drama", "acting"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilar(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama", "talent"}
	p = [][]string{{"great", "fine"}, {"acting", "drama"}, {"skills", "talent"}}
	fmt.Println(areSentencesSimilar(a, b, p))

	a = []string{"great"}
	b = []string{"great"}
	p = [][]string{}
	fmt.Println(areSentencesSimilar(a, b, p))

	a = []string{"great", "acting", "skills"}
	b = []string{"fine", "drama"}
	p = [][]string{}
	fmt.Println(areSentencesSimilar(a, b, p))
}
