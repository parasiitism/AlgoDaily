

def calMaxCallStack():
    try:
        return calMaxCallStack()+1
    except:
        return 1


# python2 999
print(calMaxCallStack())
