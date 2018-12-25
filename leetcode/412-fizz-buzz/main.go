package main

import "strconv"

// 1st approach
// WTF just beats 82.49%
// how did people do better?
func fizzBuzz(n int) []string {
	result := []string{}
	for i := 1; i <= n; i++ {
		if i%3 == 0 && i%5 == 0 {
			result = append(result, "FizzBuzz")
		} else if i%3 == 0 {
			result = append(result, "Fizz")
		} else if i%5 == 0 {
			result = append(result, "Buzz")
		} else {
			result = append(result, strconv.Itoa(i))
		}
	}
	return result
}

// 2nd approach
// in case the interviewer ask me for more mapping
// e.g.
// 3->Fizz, 5->Buzz, 7->Jazz
// beats 95.48%
func fizzBuzz1(n int) []string {
	result := []string{}
	for i := 1; i <= n; i++ {
		temp := ""
		if i%3 == 0 {
			temp += "Fizz"
		}
		if i%5 == 0 {
			temp += "Buzz"
		}
		// if i%7 == 0 {
		// 	temp += "Jazz"
		// }
		if len(temp) == 0 {
			temp = strconv.Itoa(i)
		}
		result = append(result, temp)
	}
	return result
}

func main() {

}
