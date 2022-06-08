"""


    x + 2x + 4x + 8x + ... + 2^(k-1)x = n
    x (2^0 + 2^1 + 2^2 + 2^3 + .....) = n
    x (2^k - 1) = n

    Explanaton of why
    2^0 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1) = 2^k - 1
    From binary represenation,
    2^0 = 1
    2^1 = 10
    2^2 = 100
    2^3 = 1000
    2^4 = 10000
    So, 2^0 + 2^1 + 2^2 + 2^4 = 11111 = 100000 - 1 = 2^5 - 1

    Back to the question, we just have to check if there is k, 2 <= k < 30, 
    which makes n divisible with the below equation, and that's it

    x = n / (2^k - 1)
"""


def f():
    T = int(input())
    for _ in range(T):
        n = int(input())

        for k in range(2, 30):
            divider = 2**k - 1
            if n % divider == 0:
                result = n // divider
                print(result)
                break


f()
