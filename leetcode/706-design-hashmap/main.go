package main

import (
	"fmt"
)

type MyHashMap struct {
	Arr [1000][1000]int
}

/** Initialize your data structure here. */
func Constructor() MyHashMap {
	temp := [1000][1000]int{}
	for i := 0; i < len(temp); i++ {
		for j := 0; j < len(temp[i]); j++ {
			temp[i][j] = -1
		}
	}
	return MyHashMap{temp}
}

func (this *MyHashMap) getBucket(x int) int {
	return x / 1000
}

func (this *MyHashMap) getBucketPos(x int) int {
	return x % 1000
}

/** value will always be non-negative. */
func (this *MyHashMap) Put(key int, value int) {
	i := this.getBucket(key)
	j := this.getBucketPos(key)
	this.Arr[i][j] = value
}

/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
	i := this.getBucket(key)
	j := this.getBucketPos(key)
	return this.Arr[i][j]
}

/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int) {
	i := this.getBucket(key)
	j := this.getBucketPos(key)
	this.Arr[i][j] = -1
}

func main() {
	temp := [1000][1000]int{}
	fmt.Println(len(temp))
	fmt.Println(len(temp[0]))
}
