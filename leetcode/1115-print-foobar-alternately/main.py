from threading import Lock

"""
    1st: use Mutex Lock to deal with concurrency
    keep in mind: foo(), bar() will only be called once on each cooresponding thread
    36 ms, faster than 88.31%
"""


class FooBar(object):
    def __init__(self, n):
        self.n = n

        self.fooLock = Lock()
        self.barLock = Lock()

        self.barLock.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.fooLock.acquire()
            printFoo()
            self.barLock.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.barLock.acquire()
            printBar()
            self.fooLock.release()
