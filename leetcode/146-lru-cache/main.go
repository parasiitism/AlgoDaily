package main

/*
 */

/*
	initial thought:
	- use a hashtable to store the key & value to archieve put & get Time = O(1)
	- however, we want to prioritize the items by its recency.
	1. We should need an sorted array(sorted by recency), i.e. arr = arr[i]+arr[i+1]+target
	2. how to find the key value in the sorted array? what if we store the key & index such that we can loop up from the arr easier
	3. then the look up(from arr) complexity is O(1)
	- but wait, if we remove any item from the array, we need to update the hashtable, the set time complexity will be O(n)
	- what if we store a key & the pointer of the arr in the hashtable? such that it can remove itself from the arr?
	- but then we will take O(n) to iterate the array and remove the target item...
	- what if we use a doubly linked list? so when we remove an item,
	we can just look up the node pointer(doubly linked list) from the hashtable, then set node.prev.next = node.next and node.next.prev = node.prev
	- then the put & get Time = O(1)

	class approach:
	- use a hashtable to store the key and pointer of doubly linked list node
	- use doubly linked list to prioritize the item according to its recency
	Time if put & get O(1)
	Space							O(n) n: numbder of distinct key value
	18jan2019
*/

type ListNode struct {
	Key  int
	Val  int
	Prev *ListNode
	Next *ListNode
}

type LRUCache struct {
	Cap       int
	Cnt       int
	DumpHead  *ListNode
	DumpTail  *ListNode
	HashTable map[int]*ListNode // map is reference-typed, it always pass by pointer
}

func Constructor(capacity int) LRUCache {
	head := &ListNode{-1, -1, nil, nil}
	tail := &ListNode{-1, -1, nil, nil}
	head.Next = tail
	tail.Prev = head
	return LRUCache{capacity, 0, head, tail, make(map[int]*ListNode)}
}

func (this *LRUCache) Get(key int) int {
	if v, x := this.HashTable[key]; x {
		// move to tail
		this.moveToTail(v)
		return v.Val
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if v, x := this.HashTable[key]; x {
		// move to tail
		v.Val = value
		this.moveToTail(v)
		this.HashTable[key] = v
		return
	}
	// add to tail
	node := &ListNode{key, value, nil, nil}
	this.addToTail(node)
	this.Cnt++
	// remove head if cnt > cap
	if this.Cnt > this.Cap {
		this.removeHead()
		this.Cnt--
	}
	this.HashTable[key] = node
}

func (this *LRUCache) addToTail(node *ListNode) {
	last := this.DumpTail.Prev
	last.Next = node
	node.Prev = last
	node.Next = this.DumpTail
	this.DumpTail.Prev = node
}

func (this *LRUCache) removeHead() {
	first := this.DumpHead.Next
	this.DumpHead.Next = first.Next
	first.Next.Prev = this.DumpHead
	delete(this.HashTable, first.Key)
}

func (this *LRUCache) moveToTail(node *ListNode) {
	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
	this.addToTail(node)
}

func main() {

}
