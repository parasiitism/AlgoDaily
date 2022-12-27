"""
    tedious if-else

    Tmie    O(RC)
    Space   O(RC) the buffer and the answer
"""


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        buffer = ''
        is_within_block = False
        for line in source:
            n = len(line)
            j = 0
            while j < len(line):
                c = line[j]
                # "//" -> Line comment
                if c == '/' and j+1 < n and line[j+1] == '/' and not is_within_block:
                    j = n  # Advance pointer to end of current line.
                # "/*" -> Start of block comment
                elif c == '/' and j+1 < n and line[j+1] == '*' and not is_within_block:
                    is_within_block = True
                    j += 1
                # "*/" -> End of block comment
                elif c == '*' and j+1 < n and line[j+1] == '/' and is_within_block:
                    is_within_block = False
                    j += 1
                # Normal character. Append to buffer if not in block comment
                elif not is_within_block:
                    buffer += c
                j += 1
            if buffer and not is_within_block:
                res.append(buffer)
                buffer = ''
        return res
