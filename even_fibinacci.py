#!/usr/bin/python

import unittest

m = {0: 1, 1: 1}
total = 0

def fib(n=1):
    assert n >= 0
    if n not in m:
        m[n] = fib(n-1) + fib(n-2)
    return m[n]


def even_sum_fib(exit_val=4000000):
    global total

    n = 1
    # infinite loop, but breaks when the value is above 50
    while (1) :
        value = fib(n)
        print "the value is ", value, n, exit_val
        n +=1

        if ( value % 2 == 0):
            total += value
        else:
            if value > exit_val:
                break
    return total


class TestEvenfibonacci( unittest.TestCase):
    '''
        testing the even fibonacci count
    '''
    def test_exception(self):
        self.assertRaises(AssertionError, fib, 0)

    def test_even_sum_10(self):
        self.assertEqual(even_sum_fib(10), 10 )

    def test_even_sum_10(self):
        self.assertEqual(even_sum_fib(50), 44 )

suite = unittest.TestLoader().loadTestsFromTestCase(TestEvenfibonacci)
unittest.TextTestRunner(verbosity=3).run(suite)
