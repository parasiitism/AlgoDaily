package main

import (
	"fmt"
	"strings"
)

// this is incorrect
// since when we consider "  Aa  Bb  Cc  " and ["A","B","C"], the Oj expects "  A  B  C  "
// rather than "A B C"
func replaceWords(dict []string, sentence string) string {
	result := []string{}
	words := strings.Fields(sentence)
	for i := 0; i < len(words); i++ {
		word := words[i]
		temp_result := word
		for j := 0; j < len(dict); j++ {
			dic := dict[j]
			if len(dic) > 0 && strings.HasPrefix(word, dic) && len(dic) < len(temp_result) {
				temp_result = dic
			}
		}
		result = append(result, temp_result)
	}
	return strings.Join(result, " ")
}

func main() {
	fmt.Println(strings.HasPrefix("Gopher", "Go"))
	fmt.Println(strings.HasPrefix("Gopher", "ph"))
	fmt.Println(strings.HasPrefix("Gopher", ""))
}
