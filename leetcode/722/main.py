"""
    tedious if-else

    Tmie    O(RC)
    Space   O(RC) the buffer and the answer
"""


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        N = len(source)
        real_code = ''
        is_comment = False
        res = []
        for i in range(N):
            line = source[i]
            L = len(line)
            j = 0
            while j < L:
                if line[j] == '/' and j+1 < L and line[j+1] == '/' and is_comment == False:
                    j = L
                elif line[j] == '/' and j+1 < L and line[j+1] == '*' and is_comment == False:
                    is_comment = True
                    j += 1
                elif line[j] == '*' and j+1 < L and line[j+1] == '/' and is_comment == True:
                    is_comment = False
                    j += 1
                elif is_comment == False:
                    real_code += line[j]
                j += 1
            if len(real_code) > 0 and is_comment == False:
                res.append(real_code)
                real_code = ''
        return res
