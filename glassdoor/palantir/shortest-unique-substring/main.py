"""
    Question:
    Given a list of strings, for each string, output the shortest substring that only appears in that string

    Example:
    Input: [ "palantir", "pelantors","cheapair", "cheapoair"]
    output:{
        "palantir": "ti", # ti only appears in "palantir"
        "pelantors": "s", # s only appears in "pelantors"
        "cheapair": "pai" or "apa", # either substring only appears in "cheapair"
        "cheapoair": "po" or "oa" # either substring only appears in cheapoair
    }
"""
from collections import *

"""
    1st: brute-force

    Time    O(Strs * N^3)
    Space   O(N^2)
"""


def shortest_unique(strs):
    freqs = Counter()
    for s in strs:
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                freqs[sub] += 1
    res = {}
    for s in strs:
        n = len(s)
        temp_res = []
        temp_res_length = 2**32
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if freqs[sub] == 1:
                    if len(sub) < temp_res_length:
                        temp_res_length = len(sub)
                        temp_res = [sub]
                    elif len(sub) == temp_res_length:
                        temp_res.append(sub)
        res[s] = temp_res
    return res


print(shortest_unique(["palantir", "pelantors", "cheapair", "cheapoair"]))
