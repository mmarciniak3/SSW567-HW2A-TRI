# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation


"""

import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotTri(self):
        self.assertEqual(classifyTriangle(1, 1, 5), "NotATriangle")
    def testNotTri2(self):
        self.assertEqual(classifyTriangle(1, 1, 0), "NotATriangle")
    #def testNotEqualNotTri(self):
    #    self.assertNotEqual(classifyTriangle(1, 1, 1), "NotATriangle", "Should be Equallateral")

    def testRight(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")
    #def testNotEqualRight(self):
    #    self.assertNotEqual(classifyTriangle(10, 1, 1), "Right", "Should be Not a Triangle")

    def testEqualateral(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral")
    #def testNotEqualEqualateral(self):
    #    self.assertNotEqual(classifyTriangle(3, 4, 5), "Equilateral", "Should be Right")

    def testIso(self):
        self.assertEqual(classifyTriangle(1, 3, 3), "Isoceles")
    def testIso2(self):
        self.assertEqual(classifyTriangle(2, 2, 3), "Isoceles")
    #def testNotEqualIso(self):
    #    self.assertNotEqual(classifyTriangle(2, 9, 3), "Isoceles", "Should be Not a Triangle")

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 4, 6), "Scalene")
    #def testNotEqualScalene(self):
    #    self.assertNotEqual(classifyTriangle(4, 4, 6), "Scalene", "Should be Isoceles")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

