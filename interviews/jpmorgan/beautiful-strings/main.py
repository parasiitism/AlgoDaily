"""
    When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.

    Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it.

    The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

    You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

    Input
    The input file consists of a single integer m followed by m lines.
    Output
    Your output should consist of, for each test case, a line containing the string "Case #x: y" where x is the case number (with 1 being the first case in the input file, 2 being the second, etc.) and y is the maximum beauty for that test case.
    Constraints
    5 <= m <= 50
    2 <= length of s <= 500
    
    its also a facebook hackercup question
    - https://www.facebook.com/hackercup/problem/475986555798659/
"""


def maxBeauty(s):
    ht = {}
    s = s.lower()
    for c in s:
        if c.isalpha() == False:
            continue
        if c not in ht:
            ht[c] = 1
        else:
            ht[c] += 1
    occurences = []
    for key in ht:
        occurences.append((ht[key], key))
    occurences = sorted(occurences, key=lambda x: -x[0])
    res = 0
    n = 26
    while len(occurences) > 0:
        occur, key = occurences.pop(0)
        res += occur * n
        n -= 1
    return res


print(maxBeauty('a'))
print(maxBeauty('ab'))
print(maxBeauty('abc'))
print(maxBeauty('aba'))
print(maxBeauty('abac'))
print(maxBeauty('abcc'))

print("-----")

n = int(input())
# read N lines
for i in range(n):
    s = input()  # raw_input() for python2.7
    result = maxBeauty(s)
    print(result)

"""
Input:

5
ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves
"""

"""
Output:

152
754
491
729
646
"""

"""
# fb hacker cup format
fRead = open("in.txt", "r")
fWrite = open("out.txt", "w")
t = fRead.readline()
# read N lines
i = 1
for s in fRead.readlines():
    result = maxBeauty(s)
    fWrite.write('Case #{}: {}\n'.format(i, result))
    i += 1
fWrite.close()
"""
