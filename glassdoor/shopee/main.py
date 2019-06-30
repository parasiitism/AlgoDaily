def check(func):
    def wrapper(a, b):
        if b == 0:
            print("b must not be 0!!!!")
            return
        return func(a, b)
    return wrapper


# decorate = carrying
# @check above divide() = 'divide = check(divide)'
@check
def divide(a, b):
    return a // b


print(divide(10, 0))
print(divide(10, 1))
print(divide(10, 2))
print(divide(10, 3))
