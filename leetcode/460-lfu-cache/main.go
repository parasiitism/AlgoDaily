package main

import (
	"container/heap"
	"time"
)

/*
	i cant figure the efficient way to do it
	-	learned from others
*/

type LFUCache struct {
	// 用于检查 key 的存在性
	hash map[int]*Entry
	pq   PQ
	cap  int
}

// Constructor 构建了 LFUCache
func Constructor(capacity int) LFUCache {
	return LFUCache{
		hash: make(map[int]*Entry, capacity),
		pq:   make(PQ, 0, capacity),
		cap:  capacity,
	}
}

// Get 获取 key 的值
func (this *LFUCache) Get(key int) int {
	ep, ok := this.hash[key]
	if ok {
		this.pq.update(ep)
		return ep.value
	}
	return -1
}

// Put 把 key， value 成对地放入 LFUCache
// 如果 LFUCache 已满的话，会删除掉 LFUCache 中使用最少的 key
func (this *LFUCache) Put(key int, value int) {
	if this.cap <= 0 {
		return
	}
	ep, ok := this.hash[key]
	// key 已存在，就更新 value
	if ok {
		this.hash[key].value = value
		this.pq.update(ep)
		return
	}

	ep = &Entry{key: key, value: value}
	// pq 已满的话，需要先删除，再插入
	if len(this.pq) == this.cap {
		temp := heap.Pop(&this.pq).(*Entry)
		delete(this.hash, temp.key)
	}
	this.hash[key] = ep
	heap.Push(&this.pq, ep)
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */

// entry 是 priorityQueue 中的元素
type Entry struct {
	key   int
	value int
	// 以下是辅助参数，由 heap.Interface 实现的函数自动处理
	frequence int
	index     int
	date      time.Time
}

// PQ implements heap.Interface and holds entries.
type PQ []*Entry

func (pq PQ) Len() int { return len(pq) }

func (pq PQ) Less(i, j int) bool {
	if pq[i].frequence == pq[j].frequence {
		return pq[i].date.Before(pq[j].date)
	}

	return pq[i].frequence < pq[j].frequence
}

func (pq PQ) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

// Push 往 pq 中放 entry
func (pq *PQ) Push(x interface{}) {
	n := len(*pq)
	entry := x.(*Entry)
	entry.index = n
	entry.date = time.Now()
	*pq = append(*pq, entry)
}

// Pop 从 pq 中取出最优先的 entry
func (pq *PQ) Pop() interface{} {
	old := *pq
	n := len(old)
	entry := old[n-1]
	entry.index = -1 // for safety
	*pq = old[0 : n-1]
	return entry
}

// update modifies the priority of an entry in the queue.
func (pq *PQ) update(entry *Entry) {
	entry.frequence++
	entry.date = time.Now()
	heap.Fix(pq, entry.index)
}

func main() {
	c := Constructor(2)
	c.Put(1, 1)
	// c.Put(2, 2)
	// c.Put(3, 3)
}
