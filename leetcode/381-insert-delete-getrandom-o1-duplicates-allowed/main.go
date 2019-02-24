package main

import (
	"container/list"
	"fmt"
	"math/rand"
)

/*
	learned from others
	- hashtable + linkedlist
	- https://www.youtube.com/watch?v=t5SwbbAfh-0
*/

type RandomizedCollection struct {
	rsm  map[int]*list.List
	keys []int
}

/** Initialize your data structure here. */
func Constructor() RandomizedCollection {
	return RandomizedCollection{rsm: make(map[int]*list.List), keys: make([]int, 0)}
}

/** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
func (this *RandomizedCollection) Insert(val int) bool {
	var isPresent bool
	if _, ok := this.rsm[val]; !ok {
		isPresent = true
		this.rsm[val] = list.New()
	}
	this.rsm[val].PushBack(len(this.keys))
	this.keys = append(this.keys, val)

	return isPresent
}

/** Removes a value from the collection. Returns true if the collection contained the specified element. */
func (this *RandomizedCollection) Remove(val int) bool {
	if _, ok := this.rsm[val]; !ok {
		return false
	}

	// get the first value and remove it.
	valSet := this.rsm[val]
	loc := valSet.Front().Value.(int)
	valSet.Remove(valSet.Front())
	this.rsm[val] = valSet

	if loc < len(this.keys)-1 {
		lastOne := this.keys[len(this.keys)-1]
		this.keys[loc] = lastOne

		lastOneList := this.rsm[lastOne]
		lastOneList.Remove(lastOneList.Back())
		lastOneList.PushFront(loc)
		this.rsm[lastOne] = lastOneList
	}
	this.keys = this.keys[0 : len(this.keys)-1]

	if this.rsm[val].Len() == 0 {
		delete(this.rsm, val)
	}

	return true
}

/** Get a random element from the collection. */
func (this *RandomizedCollection) GetRandom() int {
	if len(this.keys) == 0 {
		return -1
	}
	return this.keys[rand.Intn(len(this.keys))]
}

func main() {
	c := Constructor()
	c.Insert(1)
	c.Insert(1)
	c.Insert(1)
	c.Insert(2)
	c.Insert(1)
	c.Insert(2)
	c.Insert(2)
	fmt.Println(c.rsm)
	fmt.Println(c.keys)
	c.Remove(1)
	fmt.Println(c.rsm)
	fmt.Println(c.keys)
	c.Remove(1)
	// c.Remove(1)
	// c.Remove(1)
	// c.Remove(1)
	fmt.Println(c.rsm)
	fmt.Println(c.keys)
	// c.Remove(1)
	// c.Remove(3)
}
