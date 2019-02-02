package main

import (
	"container/heap"
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
	3. put the hashtable key&value into a bucket with freq as an index
	4. the first k elements are the top k elements in the bucket


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

/*
	2nd approach
	1. count num: freq into a hashtable
	2. use a heap to sort by freq order by alphabet
	3. the first k elements are the top k elements in the heap

	takeaway: sort things with priority queue using frequency WITH other params, such as 'Word'
	to accomplish `sort and order by`

	Time	O(nlogn)
	Space	O(n)
	8ms beats 100%
	2feb2019
*/
func topKFrequent1(words []string, k int) []string {
	if k > len(words) {
		return []string{}
	}
	ht := make(map[string]int)
	pq := &PriorityQueue{}
	heap.Init(pq)
	// count the freq for each num
	for _, word := range words {
		if _, x := ht[word]; x {
			ht[word]++
		} else {
			ht[word] = 1
		}
	}
	// put the num: freq into a prioroity queue
	for key, value := range ht {
		heap.Push(pq, &Item{value, key})
	}
	// pop the first k element from the priority queue
	res := []string{}
	for i := 0; i < k; i++ {
		item := heap.Pop(pq).(*Item)
		res = append(res, item.Word)
	}
	return res
}

/*
	Implement Priority Queue
*/

type Item struct {
	Freq int
	Word string
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	if pq[i].Freq == pq[j].Freq {
		return pq[i].Word < pq[j].Word
	}
	return pq[i].Freq > pq[j].Freq
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Item)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func main() {

	a := []string{}
	fmt.Println(topKFrequent1(a, 3))

	a = []string{
		"i", "love", "leetcode", "i", "love", "coding", "cat", "cat",
	}
	fmt.Println(topKFrequent1(a, 3))

	a = []string{
		"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is",
	}
	fmt.Println(topKFrequent1(a, 4))
}
