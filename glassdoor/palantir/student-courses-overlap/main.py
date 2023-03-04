from collections import *
"""
    You are a developer for a university. 
    Your current project is to develop a system for students to find courses they share with friends. 
    The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
    Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.

    e.g.1
    student_course_pairs = [
        ["58", "Software Design"],
        ["58", "Linear Algebra"],
        ["94", "Art History"],
        ["94", "Operating Systems"],
        ["17", "Software Design"],
        ["58", "Mechanics"],
        ["58", "Economics"],
        ["17", "Linear Algebra"],
        ["17", "Political Science"],
        ["94", "Economics"],
        ["25", "Economics"],
    ]

    Sample Output (pseudocode, in any order): find_pairs(student_course_pairs) =>
    {
        [58, 17]: ["Software Design", "Linear Algebra"]
        [58, 94]: ["Economics"]
        [58, 25]: ["Economics"]
        [94, 25]: ["Economics"]
        [17, 94]: []
        [17, 25]: []
    }

    e.g.2
    student_course_pairs = [
        ["42", "Software Design"],
        ["0", "Advanced Mechanics"],
        ["9", "Art History"],
    ]

    Sample output: find_pairs(student_course_pairs) =>
    {
        [0, 42]: []
        [0, 9]: []
        [9, 42]: []
    }
"""
def f(student_course_pairs):
    userset = set()
    G = defaultdict(set)
    for uid, course in student_course_pairs:
        userset.add(uid)
        G[uid].add(course)
    res = {}
    users = sorted(list(userset))
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            u1 = users[i]
            u2 = users[j]
            if u1 == u2:
                continue
            common = []
            for c in G[u1]:
                if c in G[u2]:
                    common.append(c)
            res[(u1, u2)] = common
    return res


a = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
]
print(f(a))

a = [
    ["42", "Software Design"],
    ["0", "Advanced Mechanics"],
    ["9", "Art History"],
]
print(f(a))