def findGCD(num1, num2):
    """
        Euclidian Algorithm
        - be careful of the corner cases
    """
    if num1 == num2:
        return num1
    if num1 == 0 or num2 == 0:
        return 0

    dividend = 0
    divisor = 0
    if num1 < num2:
        dividend = num2
        divisor = num1
    else:
        dividend = num1
        divisor = num2

    while True:
        mode = dividend % divisor
        if mode == 0:
            break
        else:
            dividend = divisor
            divisor = mode

    return divisor


# use the GCD
# num1 * num2 = LCM * GCD
def findLCM(num1, num2):
    return num1*num2/findGCD(num1, num2)


print(findLCM(54, 24))


# don't use GCD
# it takes a lot longer because it considers all integers
def findLCM(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if(greater % num1 == 0) and (greater % num2 == 0):
            return greater
        greater += 1


print(findLCM(54, 24))
