class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]

        1st attempt:
        1. for each line in logs, split the line by space
        2. charactorize if the 2nd word is an integer or letters, and put them into the corresponding array
        3. for letters, save an extra entity for latter sorting. 
            e.g. g1 act car => act car g1(entity)
            the reason is we have to sort from the 2nd letter first, sort the identifier in case of ties
        4. sort the letters with that entity
        5. put the letters array and digits array into the result

        Time    O(nlogn)
        Space   O(n)
        32ms beats 70.71% 
        """
        digits = []
        letters = []
        for log in logs:
            words = log.split()
            # isdigit() / isnumeric()
            if words[1].isdigit():
                digits.append(log)
            else:
                temp = ""
                for i in range(1, len(words)):
                    temp += words[i] + " "
                temp += words[0]
                letters.append((log, temp))
        letters = sorted(letters, key=lambda x: x[1])
        x = []
        for letter in letters:
            x.append(letter[0])
        return x+digits


print(Solution().reorderLogFiles(
    ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))

print(Solution().reorderLogFiles(
    ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act car"]))
