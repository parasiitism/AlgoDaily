from collections import *
"""
    https://leetcode.com/discuss/interview-question/124669/Palantir-or-Balanced-Chemical-Reactions
    
    Greedy

    e.g.1
    input:
        2H2 + O2 = 2H2O
    output:
        True, because there are 4H and 2O on both side
    
    e.g.2
    input:
        1000H2O = Au + Ag
    output:
        False, because on the left 2000H and 1000O, but on the right 1 Au and 1 Ag 

    e.g.3
    input:
        2HH2 + O2O =   3H2O
    output:
        True, because 6H and 3O on both sides
"""


def f(S):
    left, right = S.split("=")
    left_compounds = split_compounds(left)
    right_compounds = split_compounds(right)
    left_compounds_count = count_elements(left_compounds)
    right_compounds_count = count_elements(right_compounds)
    # print(left_compounds_count, right_compounds_count)
    if len(left_compounds_count.keys()) != len(right_compounds_count.keys()):
        return False
    for key in left_compounds_count:
        if key not in right_compounds_count:
            return False
        if left_compounds_count[key] != right_compounds_count[key]:
            return False
    return True


def split_compounds(S):
    compounds = S.split("+")
    return [x.strip() for x in compounds]


def count_elements(compounds):
    total = Counter()
    for compound in compounds:
        # count the elements in every compound
        ht = Counter()
        compound_count = 0
        ele = ''
        ele_count = 0
        for i in range(len(compound)):
            c = compound[i]
            if c.isdigit():
                if len(ele) == 0:
                    # the count of the compound
                    compound_count = 10*compound_count + int(c)
                else:
                    # the count of element
                    ele_count = 10*ele_count + int(c)
            elif 0 <= ord(c) - ord('A') < 26:
                # count the current element if any
                if len(ele) > 0:
                    ht[ele] += max(ele_count, 1) * max(compound_count, 1)
                    ele_count = 0
                # start with the new element
                ele = c
            elif 0 <= ord(c) - ord('a') < 26:
                ele += c
        # count the remaining element if any
        if len(ele) > 0:
            ht[ele] += max(ele_count, 1) * max(compound_count, 1)
            ele_count = 0
        # put them in total
        for key in ht:
            total[key] += ht[key]
    return total


print(f("   2H2 + O2 =   2H2O "))   # T
print(f("   1000H2O = Au + Ag "))   # F
print(f("   2HH2 + O2O =   2H2O "))   # F
print(f("   1000H2O + 2Au + 3Ag = 2Au + 3Ag + 2000H + 1000O"))  # T
