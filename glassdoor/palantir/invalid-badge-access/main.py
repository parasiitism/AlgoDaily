from collections import *
"""
    Given a list of people who enter and exit, find the people who entered without badging-out and who exited without badging-in.

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
def f(records):
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
print(f(a))