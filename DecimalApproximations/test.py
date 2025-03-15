import numpy as np
import math

n = 1_000_000

position_x = [x*2 - 1  for x in list(np.random.rand(1, n))[0]]
position_y = [x*2 - 1 for x in list(np.random.rand(1, n))[0]]

def distance_origin(x, y):
  return x**2 + y**2

def is_inside_unit_circle(x, y):
  distance = distance_origin(x, y)
  return distance <= 1

def monte_carlo_pythagoras_pi(x, y):
  points_inside = len([1 for i in range(n) if is_inside_unit_circle(position_x[i], position_y[i])])
  k = points_inside
  ratio = k/n
  return [4*ratio, 3 + k/n, k]

[pi_area_division, pi_area_subtraction, points_inside] = monte_carlo_pythagoras_pi(position_x, position_y)
k = points_inside

print("PI approximation calculated:")
print(pi_area_division)
print("\nPoints inside unit circle:")
print(points_inside)
print("\nTotal points inside unit square:")
print(n)
print("\nK/N ratio(pi/4):")
print(k/n)
print("Error in area on subtract:")
print((4 - pi_area_division) - (k/n) )
print("\nPI consistency error in area subtraction:")
print(pi_area_subtraction)
print("\nPI expected: 3.141592")

print(4*(n-k)/n)
