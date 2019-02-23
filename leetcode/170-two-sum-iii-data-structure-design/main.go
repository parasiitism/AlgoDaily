package main

/*
	questions to ask:
	- will there be duplicate number? yes
	- so if total input = [2,2], target=4, result=true? yes
	- so if total input = [2], target=2, no result since we dont count the number on the same index? yes
*/

/*
	1st approach:
	- classic 2 sum but dont count the numbers on the same indeces
	- save the occurence of each number to deal with the duplicate input

	Time	O(n)
	Space	O(n)
	100ms beats 100%
*/

type TwoSum struct {
	Arr []int
	Ht  map[int]int
}

/** Initialize your data structure here. */
func Constructor() TwoSum {
	return TwoSum{[]int{}, make(map[int]int)}
}

/** Add the number to an internal data structure.. */
func (this *TwoSum) Add(number int) {
	this.Arr = append(this.Arr, number)
	if _, x := this.Ht[number]; !x {
		this.Ht[number] = 1
	} else {
		// if the num presents more than once, just save its occurence
		this.Ht[number]++
	}
}

/** Find if there exists any pair of numbers which sum is equal to the value. */
func (this *TwoSum) Find(value int) bool {
	for _, num := range this.Arr {
		target := value - num
		if v, x := this.Ht[target]; x {
			if target != num {
				return true
			} else if v > 1 {
				// it means if there are no than one number in the hashtable
				// there must be 2 numbers on the different indeces that sum up to target
				// case: total=[2,2], target=4
				return true
			}
		}
	}
	return false
}

/**
* Your TwoSum object will be instantiated and called as such:
* obj := Constructor();
* obj.Add(number);
* param_2 := obj.Find(value);
 */

func main() {

}
