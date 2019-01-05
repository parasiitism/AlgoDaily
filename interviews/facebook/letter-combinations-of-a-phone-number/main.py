"""

   +-----+-----+-----+
   |  1  |  2  |  3  |
   |     | ABC | DEF |
   +-----------------+
   |  4  |  5  |  6  |
   | GHI | JKL | MNO |
   +-----------------+
   |  7  |  8  |  9  |
   |PQRS | TUV |WXYZ |
   +-----------------+
         |  0  |      
         |  +  |      
         +--+--+

   Write a function that given a string of numbers as input returns all possible string translations

   e.g. 1
   2 -> "A"
   22 -> "B"
   222 -> "C"
   2233 -> "BE"

   e.g. 2
   For 2223 
   2 2 2 3 -> AAAD
   22  2 3 -> BAD
   2 22  3 -> ABD
   222   3 -> CD

   Questions to ask the interviewer:
   - input only contains numbers?
        yes, 0-9 only
   - will there be a series of the same numbers in which the length is more than 3?
        yes, so for 2222, the result will be
        2 2 2 2 -> AAAA
        22  2 2 -> BAA
        2 22  2 -> ABA
        222   2 -> CA
   - so if i get input of 111111, the result will be an empty array?
        yes

"""


class Solution(object):

    def __init__(self):
        self.result = []
        self.mapping = {
            "2": "A",
            "22": "B",
            "222": "C",

            "3": "D",
            "33": "E",
            "333": "F",

            "4": "G",
            "44": "H",
            "444": "I",

            "5": "J",
            "55": "K",
            "555": "L",

            "6": "M",
            "66": "N",
            "666": "O",

            "7": "P",
            "77": "Q",
            "777": "R",
            "7777": "S",

            "8": "T",
            "88": "U",
            "888": "V",

            "9": "W",
            "99": "X",
            "999": "Y",
            "9999": "Z",
        }

    def phone_dial_combo(self, numbers):

        if len(numbers) == 0:
            return []

        """
            split the input into an array of distinct numbers
            e.g. 2223344 -> [ 222, 333, 44 ]
        """
        cur = ""
        acc = ""
        distinct_number_strs = []  # e.g. [ 2222, 333, 44 ]
        numbers += "."  # for adding the last acc in the below forloop
        for number in numbers:
            if number == cur:
                acc += number
            else:
                if len(acc) > 0:
                    distinct_number_strs.append(acc)
                cur = number
                acc = number

        """
            comput the combinations of the distinct numbers above
            , such that numbers_result = 
            [
                [AAA, BA, AB, C],   <- 222
                [DD, E],            <- 33
                [GG, H],            <- 44
            ]
        """
        numbers_result = []
        # as mentioned, the input only contains 0-9
        for distinct_number_str in distinct_number_strs:
            if distinct_number_str == "0":
                numbers_result.append(["+"])
            elif distinct_number_str == "1":
                pass  # do nothing
            elif distinct_number_str[0] == "7" or distinct_number_str[0] == "9":
                combo = self.combo(distinct_number_str, 4)
                numbers_result.append(combo)
            else:
                combo = self.combo(distinct_number_str, 3)
                numbers_result.append(combo)

        """
            cross-combine the above numbers_result
            [
                [AAA, BA, AB, C],   <- 222
                [DD, E],            <- 33
                [GG, H],            <- 44
            ]
            such that the result wil be
            [ AAADDGG, AAADDH, AAAEGG..... ]
        """
        result = [""]
        for nr in numbers_result:
            size = len(result)
            temp = []
            for i in range(size):
                for e in nr:
                    temp.append(result[i]+e)
            result = temp
        return result

    def combo(self, numbers, n_of_digits):
        """
        n_of_digits = 3 for 2,3,4,5,6,8
        n_of_digits = 4 for 7(PQRS) and 9(WXYZ)
        """
        combos = []

        def dfs(numsber_str, path):
            nonlocal combos
            if len(numsber_str) == 0:
                combos.append(path)
            else:
                for i in range(1, n_of_digits):
                    # very important: we need to check becos arr[i:] wont produce array length less than 0
                    if len(numsber_str) >= i:
                        dfs(numsber_str[i:], path+[numsber_str[:i]])
        dfs(numbers, [])

        res = []
        for combo in combos:
            s = ""
            for chars in combo:
                s += self.mapping[chars]
            res.append(s)

        return res


s = Solution()
# print(s.phone_dial_combo("2"))
# print(s.phone_dial_combo("22"))
# print(s.phone_dial_combo("222"))
# print(s.phone_dial_combo("2223"))
# print(s.phone_dial_combo("2222"))
# print(s.phone_dial_combo("22233"))
# print(s.phone_dial_combo("222233"))
# print(s.phone_dial_combo("222337"))
# print(s.phone_dial_combo("2223344"))
# print(s.phone_dial_combo("2223377"))
print(s.phone_dial_combo("04122777788"))
