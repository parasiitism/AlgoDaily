package main

/*
	1st approach:
	- dictionary + array(perserves the order) <= simulate python OrderedDict
	- hit() => put the keys in the orderdict, increment the count for existing keys
	- getHits() => count the result by iterating through the OrderedDict from back until the key <= timestamp - 300

	Time: hit()       O(1)
	Time: getHits()   O(1) cos it just counts 300 keys at maximum
	Space   O(n)
	16 ms, faster than 100.00%
*/

type HitCounter struct {
	Nums []int
	Ht   map[int]int
}

/** Initialize your data structure here. */
func Constructor() HitCounter {
	return HitCounter{[]int{}, make(map[int]int)}
}

/** Record a hit.
  @param timestamp - The current timestamp (in seconds granularity). */
func (this *HitCounter) Hit(timestamp int) {
	if _, x := this.Ht[timestamp]; !x {
		this.Nums = append(this.Nums, timestamp)
		this.Ht[timestamp] = 1
	} else {
		this.Ht[timestamp]++
	}
}

/** Return the number of hits in the past 5 minutes.
  @param timestamp - The current timestamp (in seconds granularity). */
func (this *HitCounter) GetHits(timestamp int) int {
	res := 0
	n := len(this.Nums)
	for i := n - 1; i >= 0; i-- {
		key := this.Nums[i]
		cnt := this.Ht[key]
		if key > timestamp-300 {
			res += cnt
		} else {
			delete(this.Ht, key)
			newNums := []int{}
			newNums = append(newNums, this.Nums[:i]...)
			newNums = append(newNums, this.Nums[i+1:]...)
			this.Nums = newNums

		}
	}
	return res
}

func main() {

}
