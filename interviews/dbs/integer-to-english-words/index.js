function threeDigitsToEnglish(num) {
  const digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  const tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
  let temp = ""
  const a = Math.floor(num / 100)
  if (a > 0) {
    temp += digits[a] + " Hundred "
  }
  num = num % 100
  if (num < 20) {
    temp += digits[num]
  } else {
    const b = Math.floor(num / 10)
    const c = num % 10
    temp += tens[b]
    temp += " " + digits[c]
  }
  return temp.trim()
}

console.log(threeDigitsToEnglish(0))
console.log(threeDigitsToEnglish(1))
console.log(threeDigitsToEnglish(19))
console.log(threeDigitsToEnglish(22))
console.log(threeDigitsToEnglish(90))
console.log(threeDigitsToEnglish(99))
console.log(threeDigitsToEnglish(102))
console.log(threeDigitsToEnglish(120))
console.log(threeDigitsToEnglish(900))
console.log(threeDigitsToEnglish(990))
console.log(threeDigitsToEnglish(999))

function int2eng(num) {
  const d = ["", "Thousand", "Million", "Billion"]
  let i = 0
  let res = ""
  while (true) {
    const remain = num % 1000
    const x = threeDigitsToEnglish(remain)
    if (x.length > 0) {
      res = x + " " + d[i] + " " + res
    }
    num = Math.floor(num / 1000)
    i++
    if (num == 0) {
      break
    }
  }
  res = res.trim()
  if (res.length == 0) {
    return "Zero"
  }
  return res
}

console.log(int2eng(0))
console.log(int2eng(1))
console.log(int2eng(19))
console.log(int2eng(22))
console.log(int2eng(90))
console.log(int2eng(99))
console.log(int2eng(102))
console.log(int2eng(120))
console.log(int2eng(900))
console.log(int2eng(990))
console.log(int2eng(999))

console.log(int2eng(100))
console.log(int2eng(9909))
console.log(int2eng(9912))
console.log(int2eng(9999))
console.log(int2eng(45000))
console.log(int2eng(40400))
console.log(int2eng(12500))
console.log(int2eng(12012))
console.log(int2eng(1000000))
console.log(int2eng(123456789))
console.log(int2eng(1001000000))
console.log(int2eng(1234567891))
