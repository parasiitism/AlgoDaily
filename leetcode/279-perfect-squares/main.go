package main

import (
	"fmt"
	"math"
)

type Queue struct {
	Target int
	Steps  int
}

// bfs
func numSquares(n int) int {
	if n < 2 {
		return 1
	}
	var queue []Queue
	queue = append(queue, Queue{n, 0})
	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		target := head.Target
		steps := head.Steps
		root := int(math.Sqrt(float64(target)))
		for i := 1; i <= root; i++ {
			remain := target - i*i
			if remain == 0 {
				return head.Steps + 1
			} else {
				queue = append(queue, Queue{remain, steps + 1})
			}
		}
	}
	return 1
}

func main() {
	fmt.Println(numSquares(12))
}
