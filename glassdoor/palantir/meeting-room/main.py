"""
    1st: Given a list of intevals representing some meetings, tell whether if it is possible to add a new meeting in.

    e.g.1
    Input:
        meetings = [[1300, 1500], [930, 1200],[830, 845]]
        start = 820
        end = 830

    output:
        True

    e.g.2
    Input:
        meetings = [[1300, 1500], [930, 1200],[830, 845]]
        start = 1450
        end = 1500

    output:
        False

    Questions to ask
    - is 'meetings' sorted?
    - is there already some overlap in the 'meetings'
"""
def f1_meetings_not_sorted(meetings, start, end):
    meetings.append([start, end])
    meetings.sort()
    n = len(meetings)
    for i in range(1, n):
        s1, e1 = meetings[i-1]
        s2, e2 = meetings[i]
        if e1 > s2:
            return False
    return True

print("-- f1_meetings_not_sorted --")

a = [[1300, 1500], [930, 1200],[830, 845]]
b = 820
c = 830
print(f1_meetings_not_sorted(a, b, c))

a = [[1300, 1500], [930, 1200],[830, 845]]
b = 1450
c = 1500
print(f1_meetings_not_sorted(a, b, c))

def f1_meetings_sorted(meetings, start, end):
    if end <= meetings[0][0]:
        return True

    # or we do binary search to find 2 intervals to see if we can put the new meeteing ins
    for i in range(1, n):
        s1, e1 = meetings[i-1]
        s2, e2 = meetings[i]
        if e1 >= start and end <= s2:
            return True
    
    if start >= meetings[-1][1]:
        return True

    return False

print("-- f1_meetings_sorted --")

a = [[830, 845], [930, 1200], [1300, 1500]]
b = 820
c = 830
print(f1_meetings_not_sorted(a, b, c))

a = [[830, 845], [930, 1200], [1300, 1500]]
b = 1450
c = 1500
print(f1_meetings_not_sorted(a, b, c))

"""
    2nd: Given a list of intevals representing some meetings, return the free times (from 0 to 2359)
    
    e.g.1
    Input:
        meetings = [[830, 845], [930, 1200], [1300, 1500]]

    Output:

    e.g.2
    Input:
        meetings = [[830, 930], [930, 1200], [1300, 1500]]

    Output:


    note:
    - meetings not sorted
    - there might by some intervals overlap
"""
def f2(meetings):
    meetings.sort()
    merged = []
    for s, e in meetings:
        if len(merged) > 0 and merged[-1][1] >= s:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    
    res = []
    if merged[0][0] > 0:
        res.append([0, merged[0][0]])

    for i in range(1, len(merged)):
        s1, e1 = merged[i-1]
        s2, e2 = merged[i]
        res.append([e1, s2])
    
    if merged[-1][1] < 2359:
        res.append([res[-1][1], 2359])
    
    return res

print("-- f2 --")

a = [[830, 845], [930, 1200], [1300, 1500]]
print(f2(a))

a = [[830, 930], [930, 1200], [1300, 1500]]
print(f2(a))

a = [[0,800], [830, 930], [930, 1200], [1300, 1500]]
print(f2(a))

a = [[830, 930], [930, 1200], [1300, 1500], [2358, 2359]]
print(f2(a))

a = [[0,800], [830, 930], [930, 1200], [1300, 1500], [2358, 2359]]
print(f2(a))
