# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangleangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotTri(self):
        self.assertEqual(classifyTriangle(1, 1, 5), "NotATriangle")
        self.assertNotEqual(classifyTriangle(1, 1, 1), "NotATriangle", "Should be Equallateral")

    def testRight(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")
        self.assertNotEqual(classifyTriangle(10, 1, 1), "Right", "Should be Not a Triangle")

    def testEqual(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equallateral")
        self.assertNotEqual(classifyTriangle(3, 4, 5), "Equallateral", "Should be Right")

    def testIso(self):
        self.assertEqual(classifyTriangle(1, 3, 3), "Isosceles")
        self.assertEqual(classifyTriangle(2, 2, 3), "Isosceles")
        self.assertNotEqual(classifyTriangle(2, 9, 3), "Isosceles", "Should be Not a Triangle")

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 4, 6), "Scalene")
        self.assertNotEqual(classifyTriangle(4, 4, 6), "Scalene", "Should be Isosceles")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

