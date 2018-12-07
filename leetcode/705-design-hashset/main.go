package main

/* requirements
- All values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashSet library.
*/

// naive approach:
// just based on the size give by the requirement LOL
// and it works tho it just beats 6.9%
type MyHashSet struct {
	Arr [1000000]bool
}

/** Initialize your data structure here. */
func Constructor() MyHashSet {
	return MyHashSet{[1000000]bool{}}
}

func (this *MyHashSet) Add(key int) {
	this.Arr[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.Arr[key] = false
}

/** Returns true if this set contains the specified element */
func (this *MyHashSet) Contains(key int) bool {
	return this.Arr[key]
}

func main() {

}
