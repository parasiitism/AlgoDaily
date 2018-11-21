package main

// Attempt 1: naive array
type MovingAverage struct {
	Size int
	Arr  []int
}

/** Initialize your data structure here. */
func Constructor(size int) MovingAverage {
	return MovingAverage{size, []int{}}
}

func (this *MovingAverage) Next(val int) float64 {
	this.Arr = append(this.Arr, val)
	if len(this.Arr) < this.Size {
		sum := 0
		for i := 0; i < len(this.Arr); i++ {
			sum += this.Arr[i]
		}
		return float64(sum) / float64(len(this.Arr))
	}
	sum := 0
	for i := len(this.Arr) - this.Size; i < len(this.Arr); i++ {
		sum += this.Arr[i]
	}
	return float64(sum) / float64(this.Size)
}

// Attempt 2: cache the sum
type MovingAverage1 struct {
	Size int
	Arr  []int
	Sum  int
}

func Constructor1(size int) MovingAverage1 {
	return MovingAverage1{size, []int{}, 0}
}

func (this *MovingAverage1) Next(val int) float64 {
	if len(this.Arr) < this.Size {
		this.Sum += val
		this.Arr = append(this.Arr, val)
		return float64(this.Sum) / float64(len(this.Arr))
	}
	this.Sum -= this.Arr[0]
	this.Arr = this.Arr[1:]
	this.Arr = append(this.Arr, val)
	this.Sum += val
	return float64(this.Sum) / float64(this.Size)
}

func main() {

}
