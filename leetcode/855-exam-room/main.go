package main

/*
	questions to ask:
	- how big is the N, e.g. many seats? 10^9
	- will the input leave an unocuppied seat? no for now
	- if there are more than 1 option, which should i choose?
			n = 5, seat = [1,0,1,0,1] <= choose the first 0
	- so if i remove the end or the front and more than 1 options?
			n = 4, seat = [1,0,1,0] <= choose the first 0 as always
*/

/*
	1st approach:
	- store the occupied positions in an array
	- for every seat(), check the end, the middle, and the front to find out the left most "seatable" option

	Time of seat    O(n)
	Time of leave   O(n)
	Space           O(n) worst case if all seats are occupied
	436 ms, faster than 10.88%
*/

type ExamRoom struct {
	arr []int
	n   int
}

func Constructor(N int) ExamRoom {
	return ExamRoom{[]int{}, N}
}

func (self *ExamRoom) Seat() int {
	if len(self.arr) == 0 {
		self.arr = append(self.arr, 0)
		return 0
	}
	if len(self.arr) == 1 && self.arr[0] == 0 {
		self.arr = append(self.arr, self.n-1)
		return self.n - 1
	}
	targetIdx := -1
	targetDiff := 0
	// find in the end
	if self.arr[len(self.arr)-1] != self.n-1 {
		diff := self.n - self.arr[len(self.arr)-1] - 1
		if diff >= targetDiff {
			targetDiff = diff
			targetIdx = len(self.arr) - 1
		}
	}
	// find in the middle
	for i := len(self.arr) - 2; i >= 0; i-- {
		diff := (self.arr[i+1] - self.arr[i]) / 2
		if diff >= targetDiff {
			targetDiff = diff
			targetIdx = i
		}
	}
	// find in the front
	if self.arr[0] != 0 {
		diff := self.arr[0]
		if diff >= targetDiff {
			self.arr = append([]int{0}, self.arr...)
			return 0
		}
	}
	// insert the person in the right position
	place := self.arr[targetIdx] + targetDiff
	newArr := []int{}
	newArr = append(newArr, self.arr[:targetIdx+1]...)
	newArr = append(newArr, place)
	newArr = append(newArr, self.arr[targetIdx+1:]...)
	self.arr = newArr
	return place
}

func (self *ExamRoom) Leave(p int) {
	i := 0
	for i < len(self.arr) {
		if self.arr[i] == p {
			newArr := []int{}
			newArr = append(newArr, self.arr[:i]...)
			newArr = append(newArr, self.arr[i+1:]...)
			self.arr = newArr
			break
		}
		i++
	}
}

func main() {

}
