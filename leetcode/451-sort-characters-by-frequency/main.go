package main

import "fmt"

/*
	Questions to ask:
	- only alphabeat? yes
	- capital letters and small letters should be separate?
	- empty string?

	follow-up
	- return the charactors in an alphabetic order if the frequency of characters are the same
*/

/*
	1st approach
	1. count num: freq into a hashtable
	2. put the hashtable key&value into a bucket with freq as an index
	3. append the key to the result according to a descending index order(freqency)

	Time	O(n)
	Space	O(n)
	12ms beats 66.67%
	2feb2019
*/
func frequencySort(s string) string {
	ht := make(map[rune]int)
	maxOccur := 0
	// count the freq for each char
	for _, c := range s {
		if _, x := ht[c]; x {
			ht[c]++
		} else {
			ht[c] = 1
		}
		if ht[c] > maxOccur {
			maxOccur = ht[c]
		}
	}
	// create a bucket, the index is the freq of each char
	bucket := make([][]rune, maxOccur+1)
	for key, freq := range ht {
		bucket[freq] = append(bucket[freq], key)
	}
	// append the runes to the result according to freq
	res := []rune{}
	for i := len(bucket) - 1; i >= 0; i-- {
		c := bucket[i]
		for j := 0; j < len(c); j++ {
			for k := 0; k < i; k++ {
				res = append(res, c[j])
			}
		}
	}
	return string(res)
}

/*
	another approach is to use a heap
	, but since it takes O(nlogn), im not gonna implement
*/

func main() {
	fmt.Println(frequencySort("tree"))
	fmt.Println(frequencySort("aaaccc"))
	fmt.Println(frequencySort("Aabb"))
}
