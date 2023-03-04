# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: 
@author: 
"""
def classify_triangle(side_a,side_b,side_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # require that the input values be >= 0 and <= 200
    instance_list = [isinstance(side_a, int), isinstance(side_b, int), isinstance(side_c, int)]
    if (max(side_a, side_b, side_c) > 200 or min(side_a, side_b, side_c) < 0 or not instance_list):
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if(side_a >=(side_b + side_c)) or (side_b >=(side_a + side_c)) or (side_c >=(side_a + side_b)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    elif ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2):
        return 'Right'
    elif (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    else:
        return 'Isoceles'
