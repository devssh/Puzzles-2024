




import numpy as np
import math

result = """

PI approx method chosen

Monte Carlo simulation - Pythagoras Unit Circle

- It is better method of simulation than toothpick.
- Does not need complicated sine calculation and radians calculation.
- Gives better estimate faster with no complicated math imports.

How
- Imagine unit circle of radius 1 inside a square of side length 2.
- Calculate random points x,y
- x square + y square <= 1 means inside circle, otherwise it is outside in the square.
- Using the area calculations of circle and square, deduction of pi value through reverse engineering.

- Simulate it with numpy random variables. The circle and square are imaginary. It is just a numpy matrix array.


Calculated value of PI

N = 1_000_000
K = To be measured, points outside circle.

pi/4 = points inside circle/total
pi = 4*K/N

Expected value of PI
3.14159

Accurately calculated approximate to 2-3 decimal places.
Result is pretty fast. At least faster than toothpicks.

Result is much less accurate and slower than the zeta function definition of pi.

Zeta of infinity tends towards pi, it is faster, and possibly transforms pi into a rational number of two very big numerator and denominators.

"""
n = 10_000_000

position_x = list(np.random.rand(1, n))[0]
position_y = list(np.random.rand(1, n))[0]

def distance_origin(x, y):
  return x**2 + y**2

def is_inside_unit_circle(x, y):
  distance = distance_origin(x, y)
  return distance <= 1

def monte_carlo_pythagoras_pi(x, y):
  points_inside = len([1 for i in range(n) if is_inside_unit_circle(position_x[i], position_y[i])])
  return 4*points_inside/n

pi_calculated = monte_carlo_pythagoras_pi(position_x, position_y)

print("PI approximation calculated")
print(pi_calculated)

print(result)


