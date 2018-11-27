package main

type Stack struct {
	num int
	min int
}

type MinStack struct {
	Items []Stack
}

func Constructor() MinStack {
	return MinStack{[]Stack{}}
}

func (this *MinStack) Push(x int) {
	if len(this.Items) == 0 {
		this.Items = append(this.Items, Stack{x, x})
	} else {
		lastMin := this.Items[len(this.Items)-1].min
		if x < lastMin {
			this.Items = append(this.Items, Stack{x, x})
		} else {
			this.Items = append(this.Items, Stack{x, lastMin})
		}
	}
}

func (this *MinStack) Pop() {
	this.Items = this.Items[:len(this.Items)-1]
}

func (this *MinStack) Top() int {
	return this.Items[len(this.Items)-1].num
}

func (this *MinStack) GetMin() int {
	return this.Items[len(this.Items)-1].min
}

func main() {

}
