package main

import "fmt"

/*
	1st approach:

	!!! this method is known as topological sorting/ordering !!!

	1. create a list to save to children for each node
	2. for each node, put the children in
			e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
			children list = [[], [0], [3], [], [3], [2,4,1]]
	3. use a hashtable to store the visited node, 1=visiting, 2=visited
	4. use a stack to store the nodes which no longer has unvisited children
	5. the result is the stack in the reversed order

	Time    O(V+E)
	Space   O(V)
	20ms beats 100%
*/
func findOrder(numCourses int, prerequisites [][]int) []int {
	// prepare a list to save to children for each node
	connections := [][]int{}
	for i := 0; i < numCourses; i++ {
		connections = append(connections, []int{})
	}
	// iterate though the edges and put them into the corresponding nodes in the connections
	for i := 0; i < len(prerequisites); i++ {
		prereq := prerequisites[i]
		prev := prereq[1]
		cur := prereq[0]
		connections[prev] = append(connections[prev], cur)
	}
	// iterate though the nodes and see if there is a cycle
	seen := make(map[int]int)
	stack := []int{}

	// the inner function of dfs
	var exploreVertex func(curIdx int) bool
	exploreVertex = func(curIdx int) bool {
		seen[curIdx] = 1
		children := connections[curIdx]
		for i := 0; i < len(children); i++ {
			child := children[i]
			if v, x := seen[child]; x {
				if v == 1 {
					// if seen[curIdx] == 1, it meas this node is being visiting and here is a cycle
					return false
				} else if v == 2 {
					// if seen[curIdx] == 2, it meas this node has been visited and no cycle is detected
					continue
				}
			}
			if exploreVertex(child) == false {
				return false
			}
		}
		// mark the curidx as 'visited'
		seen[curIdx] = 2
		stack = append(stack, curIdx)
		return true
	}

	for i := 0; i < numCourses; i++ {
		if v, x := seen[i]; x {
			if v == 1 {
				return []int{}
			} else if v == 2 {
				continue
			}
		}
		if exploreVertex(i) == false {
			return []int{}
		}
	}
	res := []int{}
	for i := len(stack) - 1; i >= 0; i-- {
		res = append(res, stack[i])
	}
	return res
}

/*
	2nd appraoch: Topological Ordering in BFS

	1. create a list to save to children for each node
	2. for each node, put the children in
			e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
			children list = [[], [0], [3], [], [3], [2,4,1]]
	3. count the indegree for each node(indegree = the number of incoming edges)
	4. put the nodes with 0 indegree into a queue
	5. if the queue is not empty, append the dequeued node to the result and in the same time decrement it's children's indegree
	6  after decrement, if there are nodes which has 0 indegree, put them into the queue
	7. do 6) and 7) until the queue becomes empty
	8. need a 'cnt' to check if there is a cycle(for detail: see comment)

	Time    O(V+E)
	Space   O(V)
	20ms beats 100%
*/
func findOrder1(numCourses int, prerequisites [][]int) []int {
	// prepare a list to save to children for each node
	connections := [][]int{}
	indegrees := []int{}
	for i := 0; i < numCourses; i++ {
		connections = append(connections, []int{})
		indegrees = append(indegrees, 0)
	}
	// iterate though the edges and put them into the corresponding nodes in the connections
	for i := 0; i < len(prerequisites); i++ {
		prereq := prerequisites[i]
		prev := prereq[1]
		cur := prereq[0]
		connections[prev] = append(connections[prev], cur)
		indegrees[cur]++
	}
	// put the nodes which has no incoming edges
	queue := []int{}
	for i := 0; i < numCourses; i++ {
		if indegrees[i] == 0 {
			queue = append(queue, i)
		}
	}
	// a count to check if the graph has a cycle
	// if there is a cycle, there will be a node's indegree never becomes 0
	// it means it will not be push to the queue therefore the the cnt will be inconsistent with the numCourses
	res := []int{}
	cnt := 0
	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		res = append(res, head)
		cnt++
		children := connections[head]
		for i := 0; i < len(children); i++ {
			// subtract 1 for all destinations which the current node points(prereq) to
			child := children[i]
			indegrees[child]--
			// if indegree of that child is 0, out it to the queue
			if indegrees[child] == 0 {
				queue = append(queue, child)
			}
		}
	}
	if cnt == numCourses {
		return res
	}
	return []int{}
}

func main() {
	// DFS
	fmt.Println(findOrder(6, [][]int{
		{3, 4}, {0, 1}, {2, 5}, {4, 5}, {1, 5}, {3, 2},
	}))

	fmt.Println(findOrder(6, [][]int{
		{3, 4}, {0, 1}, {2, 5}, {4, 5}, {1, 5}, {3, 2}, {5, 3},
	}))

	// BFS
	fmt.Println(findOrder1(6, [][]int{
		{3, 4}, {0, 1}, {2, 5}, {4, 5}, {1, 5}, {3, 2},
	}))

	fmt.Println(findOrder1(6, [][]int{
		{3, 4}, {0, 1}, {2, 5}, {4, 5}, {1, 5}, {3, 2}, {5, 3},
	}))
}
