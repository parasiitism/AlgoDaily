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
		return float64(sum) / float64(this.Size)
	}
	sum := 0
	for i := len(this.Arr) - this.Size; i < len(this.Arr); i++ {
		sum += this.Arr[i]
	}
	return float64(sum) / float64(this.Size)
}

func main() {

}
