#!/usr/bin/python

import unittest

def calculate_total(rangenum=4):
 
    assert(rangenum > 3 )

    '''
    Function to compute the total of multiples of 3 and 5 in the given number
    '''
    total = 0
    for number in range(3, rangenum):
        if (number % 3 == 0):
            # print "number is multiple of 3 ", number
            total += number
        elif (number % 5 == 0):
            # print "number is multiple of 5 ", number
            total += number
        else:
            next
    return total

class TestMultiples( unittest.TestCase):

    def test_exception(self):
        self.assertRaises(AssertionError, calculate_total, 3 )

    def test_under10(self):
        self.assertEqual(calculate_total(10),23)

    def test_for_number10(self):
        self.assertEqual(calculate_total(11),33)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiples)
unittest.TextTestRunner(verbosity=2).run(suite)
