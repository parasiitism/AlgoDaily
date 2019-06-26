class Car(object):
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name


a = Car(1, 'a')
b = Car(2, 'b')
c = Car(3, 'c')

t = [a, b, c]

u = [a, b, c]
print(t)

print(t == u)
