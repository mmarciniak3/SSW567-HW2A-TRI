"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation


"""

import unittest

from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """Running unittest test cases"""
    def test_not_tri(self):
        """tests if is triangle"""
        self.assertEqual(classify_triangle(1, 1, 5), "NotATriangle")
    def test_not_tri2(self):
        """tests if is triangle"""
        self.assertEqual(classify_triangle(1, 1, 0), "NotATriangle")
    def test_right(self):
        """tests if is right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
    def test_equalateral(self):
        """tests if is equal triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
    def test_iso(self):
        """tests if is iso triangle"""
        self.assertEqual(classify_triangle(1, 3, 3), "Isoceles")
    def test_iso2(self):
        """tests if is iso triangle"""
        self.assertEqual(classify_triangle(2, 2, 3), "Isoceles")
    def test_scalene(self):
        """tests if is scalene triangle"""
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()