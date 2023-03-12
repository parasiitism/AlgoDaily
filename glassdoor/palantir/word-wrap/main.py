"""
    Give a list of words and a maxLen which indicates the width of a screen, put them on the screen and separate the words by '-'
"""
def f(words, maxLen):
    lines = []
    i = 0
    while i < len(words):
        if len(words[i]) > maxLen:
            return []
        line = ''
        while i < len(words) and len(line + words[i]) + (1 if len(line) > 0 else 0) <= maxLen:
            if len(line) > 0:
                line += '-'
            line += words[i]
            i += 1
        lines.append(line)
    return lines

print(f(['calvin', 'is', 'so', 'hard', 'to', 'understand'], 12))
print(f(['calvin', 'is', 'shy'], 12))
print(f(['wertyuikjhgfdertyuilhg'], 12))
print(f(['a', 'wertyuikjhgfdertyuilhg', 'b'], 12))