package main

import (
	"fmt"
	"strconv"
)

/*
	questions to ask:
	- will there be charactors other than a-zA-Z in dictionary? yes
	- will there be duplicate words in the initial dictionary? yes
	- will there be already some duplicate abbreviated words in the initial dictionary?
	- be careful of the corner cases:
			- ["dog"], isUnique("dig") ? False
			- ["dog", "dog"], isUnique("dog") ? True
			- "dog", "dig"], isUnique("dog") ? False
*/

/*
	1st approach: hashtable
	- at init, for a new abbreviated word, save self.ht[s] = word as key:value
	- at init, for the duplicate abbreviated words, save None as value of its key, self.ht[s] = None
	- in isUnique, check if the abbreviated word exists in the hashtable

	Time    O(n)
	Space   O(n)
	88 ms, faster than 100.00%
*/
type ValidWordAbbr struct {
	M map[string]string
}

func Constructor(dictionary []string) ValidWordAbbr {
	m := make(map[string]string)
	for _, word := range dictionary {
		s := i18n(word)
		if _, x := m[s]; x {
			if m[s] != word {
				m[s] = "屌"
			}
		} else {
			m[s] = word
		}
	}
	return ValidWordAbbr{m}
}

func (this *ValidWordAbbr) IsUnique(word string) bool {
	s := i18n(word)
	if _, x := this.M[s]; x {
		if this.M[s] != word {
			return false
		}
	}
	return true
}

func i18n(s string) string {
	if len(s) < 3 {
		return s
	}
	head := s[0]
	tail := s[len(s)-1]
	cnt := strconv.Itoa(len(s) - 2)
	return string(head) + cnt + string(tail)
}

func main() {
	d := []string{"deer", "door", "cake", "card"}
	obj := Constructor(d)
	fmt.Println(obj.IsUnique("dear"))
	fmt.Println(obj.IsUnique("cart"))
	fmt.Println(obj.IsUnique("cane"))
	fmt.Println(obj.IsUnique("make"))
	fmt.Println(obj.IsUnique("door"))

	fmt.Println("--")

	d = []string{"deer", "cake", "card"}
	obj = Constructor(d)
	fmt.Println(obj.IsUnique("deer"))
	fmt.Println(obj.IsUnique("cart"))
	fmt.Println(obj.IsUnique("cane"))
	fmt.Println(obj.IsUnique("make"))
	fmt.Println(obj.IsUnique("door"))
}
