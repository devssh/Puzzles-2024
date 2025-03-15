




import numpy as np
import math

result = """

PI approx method chosen

Monte Carlo simulation - Toothpick

- Make a rectangle with random n parallel lines, width 2*w apart.
- Throw random m toothpicks of width w onto the rectange.
- Count the number of toothpicks that touch the n parallel lines (excluding the border of rectange) and call this count k.
- Pi = Total toothpicks (m) / (k) Number of toothpicks that touch the parallel lines.
- Increase m and n to get better approx. m >> n. m must be greater than n for better approx.

- Simulate it with numpy variables for toothpick location and angle. The box and toothpicks are imaginary. It is just a numpy matrix array.


Calculated value of PI

M = 10_000_000
N = 100
K = To be measured

Expected value of PI
3.14159

Accurately calculated approximate to 2 decimal places.
Result is low decimal precision because have to rely on np.sin and np.radians which use math.pi of less than 100 digits decimal accuracy.
Result is also low decimal precision for using float instead of decimal with 100 decimal accuracy.
Result for K measurement to calculate pi will be super-effective and super-fast if 
actual toothpicks are thrown in real world and a camera is used to count intersections.

By removing the limiting factor of np.sin and np.radians

sin wave can be described mathematically

sin(x) = x - x^3/3! + x^5/5! - x^7/7! ...

cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! ...

Much better result can be derived

In fact it would be better to ditch toothpicks altogether and look at the relationship between sin and pi in formula.
Toothpicks can still estimate pi from sin calculations. It is just inefficient and slow.

There are 3 popular connections between sin and complex numbers and pi
1. Gamma function
2. Reimann zeta function
3. Laplace equation and holomorphic functions

After understanding sine waves, Machin formulae using arctan might be faster.

Kikuo Takano 1982

pi/4 = 12.arctan(1/49) + 32.arctan(1/57) - 5 arctan 1/239 + 12 arctan 1/110443

F C M Stormer 1896

pi/4 = 44 arctan 1/57 + 7 arctan 1/239 - 12 arctan 1/682 + 24 arctan 1/12943

Pi is the same irrespective of base. Using this to advantage base 10 or decimal might not be the fastest way to get the digits.

Summing areas in too inefficient. Ramanujan died too early.



Arcsine calculation: Convergence - Every 5 terms in summation yield at least 3 more digits.

sin(pi/6) = 1/2

pi = 6 sininverse(1/2)

= Summation(n=0 to infty)(   (3. combination(2n -> n))  /  ((16^n).(2n + 1) )   )
where nCr = combination = 2nCn

pi = 3 + 1/8 + 9/640 + 15/7168 + 35/98304 + 189/2883584 + 693/54525952 + 429/167772160 + ...



Arctan calculation: Convergence - Every 10 additional terms yields at least 3 more digits.

4 arctan 1 = pi

Much slower than arcsin but relevant to Machin



Also look at spigot algorithms, Chudwick, Euler number(gamma), Gauss-Legendre algorithm, Leibniz formula

Really digit extraction - Simon Plouffe, Bailey - Borwein - Plouffe formula

How to Binary split arctan series in Machin's formula.

Software look at - SymPy, GNU MPFR, CLN class library for numbers
Special pi - TachusPi, y-cruncher, PiFast, QuickPi, SuperPI

Madhava, Milu, Diophantine approximation


Machin historically helped correct the lunar calendar with a better approximation of pi.Which changed dates everywhere.

"""

def sin_theta(degrees):
  return np.sin(np.radians(degrees))

def will_toothpick_cross_line(position_x, toothpick_size, angle, position_prior):
  return math.floor(position_x + toothpick_size * sin_theta(angle)) - position_prior

toothpick_count = 10_000_000
toothpick_size = 0.5
lines_measured = 100

m = toothpick_count
n = lines_measured
angle_permitted_in_degrees = 90

position = [x * n for x in list(np.random.rand(1, m))[0]]
angle = [x * angle_permitted_in_degrees for x in list(np.random.rand(1, m))[0]]

def monte_carlo_pi(m, n, position, angle): 
  position_start = [math.floor(x) for x in position]
  position_end = [will_toothpick_cross_line(x, toothpick_size, angle[i], position_start[i]) for i, x in enumerate(position)]
  k = len([x for x in position_end if x == 1])
  pi_calculated = (m / k)
  return pi_calculated

pi_calculated = monte_carlo_pi(m, n, position, angle)

print("PI approximation calculated")
print(pi_calculated)

print(result)


