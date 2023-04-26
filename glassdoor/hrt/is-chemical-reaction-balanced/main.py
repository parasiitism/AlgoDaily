from collections import *
"""
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
    print(left_compounds_count, right_compounds_count)
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
    for ele in compounds:
        # count the elements in every compound
        prefix_count = 0
        ht = Counter()
        cur = ''
        ele_count = 0
        for i in range(len(ele)):
            c = ele[i]
            if c.isdigit():
                if len(cur) == 0:
                    prefix_count = 10*prefix_count + int(c)
                else:
                    ele_count = 10*ele_count + int(c)
            elif 0 <= ord(c) - ord('A') < 26:
                if len(cur) > 0:
                    ht[cur] += max(ele_count, 1) * max(prefix_count, 1)
                    ele_count = 0
                cur = c
            elif 0 <= ord(c) - ord('a') < 26:
                cur += c
        if len(cur) > 0:
            ht[cur] += max(ele_count, 1) * max(prefix_count, 1)
            ele_count = 0
        # put them in total
        for key in ht:
            total[key] += ht[key]
    return total


print(f("   2H2 + O2 =   2H2O "))   # T
print(f("   1000H2O = Au + Ag "))   # F
print(f("   2HH2 + O2O =   2H2O "))   # T
print(f("   1000H2O + 2Au + 3Ag = 2Au + 3Ag + 2000H + 1000O"))  # T
