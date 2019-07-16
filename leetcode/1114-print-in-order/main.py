from threading import Lock
from threading import Semaphore

"""
    1st approach: use Semaphore to deal with concurrency
"""


class Foo(object):
    def __init__(self):
        self.two = Semaphore(0)
        self.three = Semaphore(0)

    def first(self, printFirst):
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.two.release()

    def second(self, printSecond):
        # printSecond() outputs "second". Do not change or remove this line.
        with self.two:
            printSecond()
            self.three.release()

    def third(self, printThird):
        # printThird() outputs "third". Do not change or remove this line.
        with self.three:
            printThird()


"""
    2nd approach: use Mutex Lock to deal with concurrency
"""


class Foo(object):
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst):
        printFirst()
        self.lock1.release()

    def second(self, printSecond):
        with self.lock1:
            printSecond()
            self.lock2.release()

    def third(self, printThird):
        with self.lock2:
            printThird()
