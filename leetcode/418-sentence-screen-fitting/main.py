class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        res = []
        line = ""

        cnt = 0

        while True:
            shouldBreak = False
            for word in sentence:
                l_w = len(word)
                l_l = len(line)
                if l_w == cols:
                    if l_l > 0:
                        res.append(line)
                        # rows
                        rows -= 1
                        if rows == 0:
                            shouldBreak = True
                            break
                        # rows
                    line = word
                elif l_w > cols:
                    shouldBreak = True
                    break
                else:
                    if l_w + 1 + l_l > cols:
                        res.append(line)
                        # rows
                        rows -= 1
                        if rows == 0:
                            shouldBreak = True
                            break
                        # rows
                        line = word
                    else:
                        if len(line) == 0:
                            line = word
                        else:
                            line += "-" + word
            # if len(line) > 0:
            #     res.append(line)

            if shouldBreak == True:
                break

            cnt += 1

        return res, cnt


print(Solution().wordsTyping(["hello"], 4, 4))
print(Solution().wordsTyping(["hell", "hello"], 4, 4))
print(Solution().wordsTyping(["hello"], 4, 5))
print(Solution().wordsTyping(["hello", "world"], 2, 8))
print(Solution().wordsTyping(["a", "bcd", "e"], 3, 6))
print(Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 5))
print(Solution().wordsTyping(["try", "to", "be", "better"], 17, 2))
print(Solution().wordsTyping(["a", "b", "e"], 20000, 20000))
