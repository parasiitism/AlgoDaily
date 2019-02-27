package main

import (
	"fmt"
	"strings"
)

/*
	1st approach:
	1. separate the numbers by 3 didgits, 123456789 -> 123, 456, 789
	2. for each 3 digits, translate to english
	3. for append Thousand, Million and Billion for each iteration of division

	Time		O(n)
	Space		O(n)
	0 ms, faster than 100.00%
	26feb2019
*/
func numberToWords(num int) string {
	d := []string{"", "Thousand", "Million", "Billion"}
	temp := ""
	i := 0
	for true {
		remain := num % 1000
		num = num / 1000
		threeDigitsWords := threeDigitsToWords(remain)
		if len(threeDigitsWords) > 0 {
			temp = threeDigitsWords + " " + d[i] + " " + temp
		}
		i++
		if num == 0 {
			break
		}
	}
	temp = strings.TrimSpace(temp)
	if len(temp) == 0 {
		return "Zero"
	}
	return temp
}

func threeDigitsToWords(num int) string {
	digits := []string{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
		"Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
	tens := []string{"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}
	a := num / 100
	num = num % 100
	temp := ""
	if a > 0 {
		temp += digits[a] + " Hundred "
	}
	if num < 20 {
		temp += digits[num]
	} else {
		b := num / 10
		num = num % 10
		temp += tens[b]
		temp += " " + digits[num]
	}
	return strings.TrimSpace(temp)
}

func main() {
	fmt.Println(threeDigitsToWords(999))
	fmt.Println(threeDigitsToWords(990))
	fmt.Println(threeDigitsToWords(900))
	fmt.Println(threeDigitsToWords(120))
	fmt.Println(threeDigitsToWords(102))
	fmt.Println(threeDigitsToWords(919))
	fmt.Println(threeDigitsToWords(99))
	fmt.Println(threeDigitsToWords(50))
	fmt.Println(threeDigitsToWords(20))
	fmt.Println(threeDigitsToWords(19))
	fmt.Println(threeDigitsToWords(10))
	fmt.Println(threeDigitsToWords(1))
	fmt.Println(threeDigitsToWords(0))

	fmt.Println(numberToWords(999))
	fmt.Println(numberToWords(990))
	fmt.Println(numberToWords(900))
	fmt.Println(numberToWords(120))
	fmt.Println(numberToWords(102))
	fmt.Println(numberToWords(919))
	fmt.Println(numberToWords(99))
	fmt.Println(numberToWords(50))
	fmt.Println(numberToWords(20))
	fmt.Println(numberToWords(19))
	fmt.Println(numberToWords(10))
	fmt.Println(numberToWords(1))
	fmt.Println(numberToWords(0))
	fmt.Println(numberToWords(1000))
	fmt.Println(numberToWords(9909))
	fmt.Println(numberToWords(9912))
	fmt.Println(numberToWords(9999))
	fmt.Println(numberToWords(45000))
	fmt.Println(numberToWords(40400))
	fmt.Println(numberToWords(12500))
	fmt.Println(numberToWords(12012))
	fmt.Println(numberToWords(1000000))
	fmt.Println(numberToWords(1234567))
	fmt.Println(numberToWords(1001000000))
	fmt.Println(numberToWords(1234567891))
}
