def f():
    T = int(input())
    for _ in range(T):
        A = [c for c in input()]
        B = [c for c in input()]
        A.reverse()
        B.reverse()
        while len(A) > 0 and len(B) > 0:
            if A[0] == B[0]:
                A.pop(0)
                B.pop(0)
            else:
                if len(A) > 1:
                    A.pop(0)
                    A.pop(0)
                else:
                    A.pop(0)
        if len(B) == 0:
            print("YES")
        else:
            print("NO")


# print(solve("ababa", "ba"))
# print(solve("ababa", "bb"))
# print(solve("aaa", "aaaa"))
# print(solve("aababa", "ababa"))

f()
