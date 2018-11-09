package main

import (
	"fmt"
)

type MapSum struct {
	Val      int
	Children map[string]*MapSum
}

/** Initialize your data structure here. */
func Constructor() MapSum {
	return MapSum{0, make(map[string]*MapSum)}
}

func (this *MapSum) Insert(key string, val int) {
	current := this
	for i := 0; i < len(key); i++ {
		charactor := string(key[i])
		var temp *MapSum
		if value, existed := current.Children[charactor]; existed {
			temp = value
		} else {
			temp = &MapSum{0, make(map[string]*MapSum)}
		}
		if i == len(key)-1 {
			temp.Val = val
		}
		current.Children[charactor] = temp
		current = temp
	}
}

func (this *MapSum) StartsWith(prefix string) *MapSum {
	current := this
	for i := 0; i < len(prefix); i++ {
		charactor := string(prefix[i])
		if value, existed := current.Children[charactor]; existed {
			if i == len(prefix)-1 {
				return value
			}
			current = value
		} else {
			return nil
		}
	}
	return nil
}

func (this *MapSum) Sum(prefix string) int {
	target := this.StartsWith(prefix)
	if target == nil {
		return 0
	}
	result := 0
	var stack []*MapSum
	stack = append(stack, target)
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result += pop.Val
		for _, v := range pop.Children {
			stack = append(stack, v)
		}
	}
	return result
}

func main() {
	obj := Constructor()
	obj.Insert("a", 3)
	fmt.Println(obj.Sum("a"))
	obj.Insert("ap", 3)
	fmt.Println(obj.Sum("a"))
	obj.Insert("ap", 3)
	fmt.Println(obj.Sum("a"))
}
