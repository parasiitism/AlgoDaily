package main

import (
	"fmt"
	"strings"
)

// honestly, i think this is incorrect
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
	// if we can just use "strings.Join", what if the original sentence has multiple space in a row?
	return strings.Join(result, " ")
}

// correct but it is too slow, although it doesnt result in TLE
func replaceWords1(dict []string, sentence string) string {
	i := 0
	j := 0
	result := ""
	for true {
		if string(sentence[j]) == " " {
			result += " "
			i++
			j++
			if j == len(sentence) {
				break
			}
		} else {
			j++
			if j == len(sentence) {
				word := sentence[i:j]
				temp_result := sentence[i:j]
				for k := 0; k < len(dict); k++ {
					dic := dict[k]
					if len(dic) > 0 && strings.HasPrefix(word, dic) && len(dic) < len(temp_result) {
						temp_result = dic
					}
				}
				result += temp_result
				break
			}
			if string(sentence[j]) == " " {
				word := sentence[i:j]
				temp_result := sentence[i:j]
				for k := 0; k < len(dict); k++ {
					dic := dict[k]
					if len(dic) > 0 && strings.HasPrefix(word, dic) && len(dic) < len(temp_result) {
						temp_result = dic
					}
				}
				result += temp_result
				i = j
			}
		}
	}
	return result
}

func main() {
	d := []string{"cat", "bat", "rat", "ra"}
	s := "the cattle was rattled by , the  battery"
	fmt.Println(replaceWords1(d, s))
}
