package main

import (
	"math/rand"
	"time"
)

/*
	questions to ask:
	- each item means each the items inserted or the key inserted? allow duplicate?

	1st approach: hashtable

	Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		O(n)
	Space							O(n) the unique keys
	1336 ms, faster than 6.52%
*/

type RandomizedSet struct {
	HashTable map[int]bool
}

/** Initialize your data structure here. */
func Constructor() RandomizedSet {
	return RandomizedSet{make(map[int]bool)}
}

/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
	if _, x := this.HashTable[val]; x {
		return false
	}
	this.HashTable[val] = true
	return true
}

/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
	if _, x := this.HashTable[val]; x {
		delete(this.HashTable, val)
		return true
	}
	return false
}

/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
	rand.Seed(time.Now().UTC().UnixNano())
	n := len(this.HashTable)
	targetIdx := rand.Intn(n)
	keys := []int{}
	for k, _ := range this.HashTable {
		keys = append(keys, k)
	}
	key := keys[targetIdx]
	return key
}

func main() {
}
