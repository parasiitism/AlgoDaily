package main

/* requirements
- All values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashSet library.
*/

// naive approach 1:
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

// naive approach 2:
// i saw this on Discussion
// actually it makes no sense cox it just transforms the 1D array to a 2D array
// beats 51.72%
type MyHashSet1 struct {
	Arr [1000][1000]bool
}

func (this *MyHashSet1) getBucket(x int) int {
	return x / 1000
}

func (this *MyHashSet1) getBucketPos(x int) int {
	return x % 1000
}

/** Initialize your data structure here. */
func Constructor1() MyHashSet1 {
	return MyHashSet1{[1000][1000]bool{}}
}

func (this *MyHashSet1) Add1(key int) {
	i := this.getBucket(key)
	j := this.getBucketPos(key)
	this.Arr[i][j] = true
}

func (this *MyHashSet1) Remove1(key int) {
	i := this.getBucket(key)
	j := this.getBucketPos(key)
	this.Arr[i][j] = false
}

/** Returns true if this set contains the specified element */
func (this *MyHashSet1) Contains1(key int) bool {
	i := this.getBucket(key)
	j := this.getBucketPos(key)
	return this.Arr[i][j]
}

func main() {

}
