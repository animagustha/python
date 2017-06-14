"""Demonstrates functions

Write a python program that calculates slope of a line
"""


def slope(point):
    m = (point[1][1] - point[0][1])/(point[1][0] - point[0][0])
    return m
points = [[1, 2], [3, 4]]
a = slope(points)

print('slope for the line', points[0], points[1], 'is', a)
