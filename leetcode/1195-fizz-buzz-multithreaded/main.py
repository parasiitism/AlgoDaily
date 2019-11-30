from threading import Lock

"""
    1st: use Mutex Lock to deal with concurrency
    keep in mind: foo(), bar() will only be called once on each cooresponding thread
    20 ms, faster than 83.23% 
"""


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n

        self.numLock = Lock()
        self.fizzLock = Lock()
        self.buzzLock = Lock()
        self.fizzbuzzLock = Lock()

        self.fizzLock.acquire()
        self.buzzLock.acquire()
        self.fizzbuzzLock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 > 0:
                self.fizzLock.acquire()
                printFizz()
                self.numLock.release()

    # printBuzz() outputs "buzz"

    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 > 0 and i % 5 == 0:
                self.buzzLock.acquire()
                printBuzz()
                self.numLock.release()

    # printFizzBuzz() outputs "fizzbuzz"

    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzLock.acquire()
                printFizzBuzz()
                self.numLock.release()

    # printNumber(x) outputs "x", where x is an integer.

    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            self.numLock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzLock.release()
            elif i % 3 == 0:
                self.fizzLock.release()
            elif i % 5 == 0:
                self.buzzLock.release()
            else:
                printNumber(i)
                self.numLock.release()
