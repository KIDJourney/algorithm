from threading import Lock


class Foo(object):
    def __init__(self):
        self.stage = 0
        self.lock = Lock()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        while True:
            with self.lock.acquire():
                if self.stage == 0:
                    printFirst()
                    self.stage += 1
                    break

        # printFirst() outputs "first". Do not change or remove this line.

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() outputs "second". Do not change or remove this line.
        while True:
            with self.lock.acquire():
                if self.stage == 1:
                    printSecond()
                    self.stage += 1
                    break

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while True:
            with self.lock.acquire():
                if self.stage == 2:
                    printThird()
                    self.stage += 1
                    break

        # printThird() outputs "third". Do not change or remove this line.
