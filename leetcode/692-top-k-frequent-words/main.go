package main

import (
	"fmt"
	"sort"
)

/*
	Questions to ask:
	- will there will element has the same frequency? alphabetical order
*/

/*
	1st approach
	1. count num: freq into a hashtable
	2. sort the hashtable keys
	2. put the hashtable key&value into a bucket with freq as an index
	3. the first k elements are the top k elements in the bucket


	Time	O(nlogn)
	Space	O(n)
	12ms beats 25%
	2feb2019
*/
func topKFrequent(words []string, k int) []string {
	if k > len(words) {
		return []string{}
	}
	ht := make(map[string]int)
	maxOccur := 0
	// count the freq for each num
	for _, word := range words {
		if _, x := ht[word]; x {
			ht[word]++
		} else {
			ht[word] = 1
		}
		if ht[word] > maxOccur {
			maxOccur = ht[word]
		}
	}
	// create a bucket, the index is the freq of nums
	bucket := make([][]string, maxOccur+1)
	// sort the keys
	keys := []string{}
	for key := range ht {
		keys = append(keys, key)
	}
	sort.Strings(keys)
	for _, key := range keys {
		freq := ht[key]
		bucket[freq] = append(bucket[freq], key)
	}
	// get the most frequent k
	res := []string{}
	j := 0
	for i := len(bucket) - 1; i >= 0; i-- {
		strs := bucket[i]
		for _, str := range strs {
			if j < k {
				res = append(res, str)
				j++
			}
		}
	}

	return res
}

func main() {

	a := []string{}
	fmt.Println(topKFrequent(a, 3))

	a = []string{
		"i", "love", "leetcode", "i", "love", "coding", "cat", "cat",
	}
	fmt.Println(topKFrequent(a, 2))

	a = []string{
		"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is",
	}
	fmt.Println(topKFrequent(a, 4))
}
