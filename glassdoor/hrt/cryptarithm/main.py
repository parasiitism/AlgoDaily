def count_cryptarithms(words):
    a, b, c = words[0], words[1], words[2]
    if max(len(a), len(b)) > len(c):
        return 0
    all_chars = set()
    heads = set()
    clone = []
    for w in words:
        for i in range(len(w)):
            c = w[i]
            all_chars.add(c)
            if i == 0:
                heads.add(c)
        clone.append(w[::-1])
    words = clone
    used_digits = 10 * [False]

    def backtracking(i, j):
