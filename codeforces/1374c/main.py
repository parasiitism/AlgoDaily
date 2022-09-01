def f():
    n = int(input())
    for _ in range(n):
        _ = input()
        s = input()
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        print(len(stack) // 2)


f()
