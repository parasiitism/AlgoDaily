class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        d = ["", "Thousand", "Million", "Billion"]
        result = ""
        i = 0
        while True:
            remain = num % 1000
            num = num / 1000
            threeDigitWord = self.threeDigitsToWords(remain)
            if len(threeDigitWord) > 0:
                result = threeDigitWord + " " + d[i] + " " + result
            i += 1
            if num == 0:
                break
        return result.strip()

    def threeDigitsToWords(self, num):
        digits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                  "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        a = num / 100
        num = num % 100
        temp = ""
        if a > 0:
            temp += digits[a] + " Hundred "
        if num < 20:
            temp += digits[num]
        else:
            b = num / 10
            c = num % 10
            temp += tens[b]
            temp += " " + digits[c]
        return temp.strip()
