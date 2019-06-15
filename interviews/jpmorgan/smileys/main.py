"""
Your friend John uses a lot of emoticons when you talk to him on Messenger. In addition to being a person who likes to express himself through emoticons, he hates unbalanced parenthesis so much that it makes him go :(

Sometimes he puts emoticons within parentheses, and you find it hard to tell if a parenthesis really is a parenthesis or part of an emoticon.

A message has balanced parentheses if it consists of one of the following:

- An empty string ""
- One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
- An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'.
- A message with balanced parentheses followed by another message with balanced parentheses.
- A smiley face ":)" or a frowny face ":("
Write a program that determines if there is a way to interpret his message while leaving the parentheses balanced.

Input
The first line of the input contains a number T (1 ≤ T ≤ 50), the number of test cases. 
The following T lines each contain a message of length s that you got from John.

Output
For each of the test cases numbered in order from 1 to T, output "Case #i: " followed by a string stating whether or not it is possible that the message had balanced parentheses. If it is, the string should be "YES", else it should be "NO" (all quotes for clarity only)

Constraints
1 <= length of s <= 100

its also a fb hacker cup question
- https://www.facebook.com/hackercup/problem/403525256396727/
"""


def is_balanced(s):
    minOpen = 0
    maxOpen = 0
    for c in s:
        if c == '(':
            minOpen += 1
            maxOpen += 1
        elif c == ')':
            # if the best we can do still cant satisfy the ), the total parentheses are not balanced
            if maxOpen == 0:
                return False
            # we want to make sure that minOpen >= 0, so cant minOpen -= 1
            minOpen = max(minOpen-1, 0)
            maxOpen -= 1
        elif c == '{':
            # {} means, optionally, we regard :( as (, so maximize the maxOpenCnt by inrementing 1
            maxOpen += 1
        elif c == '}':
            # } means, optionally, we regard :) as ), so minimize the minOpenCnt by decrementing 1
            # we want to make sure that minOpen >= 0, so cant minOpen -= 1
            minOpen = max(minOpen-1, 0)
    # return minOpen <= 0 <= maxOpen
    return minOpen == 0 and minOpen <= maxOpen


def check(s):
    s = s.replace(':)', '}')
    s = s.replace(':(', '{')
    return is_balanced(s)


print(check('hacker cup: started :):)'))
print(check('(:)'))
print(check('i am sick today (:()'))
print(check(')('))
print(check(':(('))

print('-----')

n = int(input())
for i in range(n):
    s = input()  # raw_input() for python2.7
    result = check(s)
    print(result)

"""
5
hacker cup: started :):)
(:)
i am sick today (:()
)(
:((
"""

"""
# fb hacker cup format
fRead = open("in.txt", "r")
fWrite = open("out.txt", "w")
t = fRead.readline()
# read N lines
i = 1
for s in fRead.readlines():
    result = check(s)
    fWrite.write('Case #{}: {}\n'.format(
        i, 'YES' if result == True else 'NO'))
    i += 1
fWrite.close()
"""
