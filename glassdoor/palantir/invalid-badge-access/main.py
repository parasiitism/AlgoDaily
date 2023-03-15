from collections import *
"""
    1st: Given a list of people who enter and exit, find the people who entered without badging-out and who exited without badging-in.

    badge_records = [
        ["Martha",   "exit"],
        ["Paul",     "enter"],
        ["Martha",   "enter"],
        ["Martha",   "exit"],
        ["Jennifer", "enter"],
        ["Paul",     "enter"],
        ["Curtis",   "enter"],
        ["Paul",     "exit"],
        ["Martha",   "enter"],
        ["Martha",   "exit"],
        ["Jennifer", "exit"],
    ]
    output: [["Martha"], ["Paul", "Curtis"]]
"""
def f1(records):
    ht = defaultdict(list)
    for name, inout in records:
        if name in ht:
            if ht[name][-1] == 'enter' and inout == 'exit':
                ht[name].pop()
            else:
                ht[name].append(inout)
        else:
            ht[name].append(inout)
    entered_without_badging_out = set()
    exited_without_badging_in = set()
    for name in ht:
        for inout in ht[name]:
            if inout == 'enter':
                exited_without_badging_in.add(name)
            else:
                entered_without_badging_out.add(name)
    return (entered_without_badging_out, exited_without_badging_in)


a = [
    ["Martha",   "exit"],
    ["Paul",     "enter"],
    ["Martha",   "enter"],
    ["Martha",   "exit"],
    ["Jennifer", "enter"],
    ["Paul",     "enter"],
    ["Curtis",   "enter"],
    ["Paul",     "exit"],
    ["Martha",   "enter"],
    ["Martha",   "exit"],
    ["Jennifer", "exit"],
]
print(f1(a))

"""
    2nd:
    Given a list of people who swipe their badge, return the people who frequently swipe their badge within an hour and the times involved

    e.g.
    [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1630']]

    output:
    {
        'Martha': ['1600', '1620', '1530']
    }
"""
def f2(records):
    ht = defaultdict(list)
    res = defaultdict(list)
    for n, t in records:
        t = int(t)
        if n in ht:
            if t - ht[n][-1] < 100:
                if len(res[n]) > 0 and res[n][-1] == ht[n][-1]:
                    res[n].append(t)
                else:
                    res[n].append(ht[n][-1])
                    res[n].append(t)
        ht[n].append(t)
    return res

a = [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1630']]
print(f2(a))
