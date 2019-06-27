package main

import "fmt"

/*
	Round Robin Scheduling
	- https://www.youtube.com/watch?v=aWlQYllBZDs
	- https://wdxtub.com/interview/14520850399861.html

	Detail:
	- each task has one arrival time and one execution time, arrivals & executions are paired up already in a correct order for you
	- the input arrival times are sorted
	- return the average waiting time for each task

	Caution:
	- cant use priority queue, because if one item's arrival time is the same is another one item's remain, priority might mess up
*/

type Task struct {
	ArrTime int
	ExcTime int
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/*
	1st approach
	- use a queue
	- put the first item first
*/
func roundRobin1(arrivals []int, executions []int, quantum int) float64 {
	if len(arrivals) == 0 || len(executions) == 0 || len(arrivals) != len(executions) {
		return 0
	}
	var q []*Task
	curTime := 0
	totalWait := 0
	// put the first item in the queue
	q = append(q, &Task{arrivals[0], executions[0]})
	i := 1
	// process the queue
	for len(q) > 0 {
		// pop the item from the queue with minimum arr
		task := q[0]
		q = q[1:]
		// if the item arr > curTime, update the cur time
		if task.ArrTime > curTime {
			curTime = task.ArrTime
		}
		// current time - arr is the waiting time of this item
		totalWait += curTime - task.ArrTime
		// task got done, update the current time
		curTime += findMin(quantum, task.ExcTime)
		// put the tasks to the queue which the arrival time < current time
		for i < len(arrivals) && arrivals[i] <= curTime {
			q = append(q, &Task{arrivals[i], executions[i]})
			i++
		}
		// determin if we need to execute this item in the next round
		if task.ExcTime > quantum {
			q = append(q, &Task{curTime, task.ExcTime - quantum})
		}
	}
	return float64(totalWait) / float64(len(arrivals))
}

/*
	2nd approach
	- use a queue
	- put the items in the loop
*/
func roundRobin2(arrivals []int, executions []int, quantum int) float64 {
	if len(arrivals) == 0 || len(executions) == 0 || len(arrivals) != len(executions) {
		return 0
	}
	var q []*Task
	curTime := 0
	totalWait := 0
	i := 0
	// process the queue
	for len(q) > 0 || i < len(arrivals) {
		if len(q) > 0 {
			// pop the item from the queue with minimum arr
			task := q[0]
			q = q[1:]
			// current time - arr is the waiting time of this item
			totalWait += curTime - task.ArrTime
			// task got done, update the current time
			curTime += findMin(quantum, task.ExcTime)
			// put the tasks to the queue which the arrival time < current time
			for i < len(arrivals) && arrivals[i] <= curTime {
				q = append(q, &Task{arrivals[i], executions[i]})
				i++
			}
			// determin if we need to execute this item in the next round
			if task.ExcTime > quantum {
				q = append(q, &Task{curTime, task.ExcTime - quantum})
			}
		} else {
			q = append(q, &Task{arrivals[i], executions[i]})
			curTime = arrivals[i]
			i++
		}
	}
	return float64(totalWait) / float64(len(arrivals))
}

func main() {
	a0 := []int{0, 1, 3, 5, 6}
	a1 := []int{0, 1, 2, 3}
	a2 := []int{0, 1, 4}

	e0 := []int{5, 3, 6, 1, 4}
	e1 := []int{5, 3, 8, 6}
	e2 := []int{5, 2, 3}
	// 6.4
	fmt.Println(roundRobin1(a0, e0, 3))
	// 8.5
	fmt.Println(roundRobin1(a1, e1, 3))
	// 6.4
	fmt.Println(roundRobin1(a2, e2, 3))

	// 6.4
	fmt.Println(roundRobin2(a0, e0, 3))
	// 8.5
	fmt.Println(roundRobin2(a1, e1, 3))
	// 6.4
	fmt.Println(roundRobin2(a2, e2, 3))
}
