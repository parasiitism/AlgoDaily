package main

import (
	"fmt"
	"unicode"
)

/*
	1st approach:
	- use 2 stacks
	- the basic idea is to save each operator with the level of parenthesis, see type OpStack
	- when there is a ), sum up the result on the same parenthesis level, and decrement the global parenthesis level

	e.g. 1+2-(3+4-(5+6))+7
	iterations on each token:
	1:	numstack = [1]
	+:	opstack = [(+,0)]
	2:	numstack = [1,2]
	-:	opstack = [(+,0),(-,0)]
	(:	parenthesesCount 0->1
	3:	numstack = [1,2,3]
	+:	opstack = [(+,0),(-,0),(+,1)]
	4:	numstack = [1,2,3,4]
	-:	opstack = [(+,0),(-,0),(+,1),(-,1)]
	(:	parenthesesCount 1->2
	5:	numstack = [1,2,3,4,5]
	+:	opstack = [(+,0),(-,0),(+,1),(-,1),(+,2)]
	6:	numstack = [1,2,3,4,5,6]
	):	numstack = [1,2,3,4,11], opstack = [(+,0),(-,0),(+,1),(-,1)], parenthesesCount 2->1
	):	numstack = [1,2,-4], opstack = [(+,0),(-,0)], parenthesesCount 1->0
	+:	opstack = [(+,0),(-,0),(+,0)]
	7+	numstack = [1,2,-4,7]
	end: iterate the numstack and calculate 1+2-(-4)+7=>14

	Time	O(2n) the nested loop actually just runs one time time
	Space O(n)
	28 ms, faster than 25.49%
*/

type OpStack struct {
	operator byte
	level    int
}

func calculate(s string) int {

	parenthesesCount := 0
	operatorStack := []OpStack{}
	numberStack := []int{}
	i := 0
	for i < len(s) {
		if unicode.IsDigit(rune(s[i])) == true {
			curNum := 0
			j := i
			for j < len(s) && unicode.IsDigit(rune(s[j])) == true {
				curNum = curNum*10 + int(s[j]) - 48
				j++
			}
			numberStack = append(numberStack, curNum)
			i = j
			continue
		}
		if s[i] == '+' || s[i] == '-' {
			operatorStack = append(operatorStack, OpStack{s[i], parenthesesCount})
		}
		if s[i] == '(' {
			parenthesesCount++
		}
		if s[i] == ')' {
			if len(operatorStack) == 0 {
				parenthesesCount--
				i++
				continue
			}

			level := operatorStack[len(operatorStack)-1].level
			arr := []int{}
			operators := []byte{}

			pop := numberStack[len(numberStack)-1]
			numberStack = numberStack[:len(numberStack)-1]
			arr = append([]int{pop}, arr...)
			for len(operatorStack) > 0 && operatorStack[len(operatorStack)-1].level == level {
				pop := numberStack[len(numberStack)-1]
				numberStack = numberStack[:len(numberStack)-1]
				arr = append([]int{pop}, arr...)

				popOp := operatorStack[len(operatorStack)-1]
				operatorStack = operatorStack[:len(operatorStack)-1]
				operators = append([]byte{popOp.operator}, operators...)
			}

			temp := 0
			op := '+'
			for _, num := range arr {
				if op == '+' {
					temp += num
				} else if op == '-' {
					temp -= num
				}
				if len(operators) > 0 {
					op = rune(operators[0])
					operators = operators[1:]
				}
			}
			numberStack = append(numberStack, temp)
			parenthesesCount--
		}
		i++
	}

	temp := numberStack[0]
	numberStack = numberStack[1:]

	for len(operatorStack) > 0 {
		op := rune(operatorStack[0].operator)
		operatorStack = operatorStack[1:]

		pop := numberStack[0]
		numberStack = numberStack[1:]
		if op == '+' {
			temp += pop
		} else if op == '-' {
			temp -= pop
		}
	}

	return temp
}

func main() {
	fmt.Println(calculate("1+2"))
	fmt.Println(calculate("1-2"))

	fmt.Println(calculate("(3)"))
	fmt.Println(calculate("1-(2-3)"))
	fmt.Println(calculate(" 2-1 + 2 "))
	fmt.Println(calculate("(1+(4+5+2)-3)+(6+8)"))
}
