from threading import Semaphore

"""
    approach: use Semaphore to deal with concurrency
"""


class Foo(object):
    def __init__(self):
        self.two = Semaphore(0)
        self.three = Semaphore(0)

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.two.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        # printSecond() outputs "second". Do not change or remove this line.
        with self.two:
            printSecond()
            self.three.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        # printThird() outputs "third". Do not change or remove this line.
        with self.three:
            printThird()
