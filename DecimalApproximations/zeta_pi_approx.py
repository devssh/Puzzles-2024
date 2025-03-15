


from decimal import *

getcontext().prec = 100

def piN(n):
  acc = Decimal('0')
  for i in range(n):
    acc = acc + Decimal('1')/(Decimal(str(i + 1))**Decimal('4'))
  acc = acc * Decimal('90')
  return acc**Decimal('0.25')


results = """
PI Approximation Techniques

- chosen

Zeta(4)

(1/1)^4 + (1/2)^4 + (1/3)^4 + ... inf = (pi^4)/90

3.141592653589793238462401496807536861846770548886445923904285738450298318525506090967879347475729222

Correct Match upto
3.141592653589793238462

21 decimal places correct of pi for N = 10_000_000 instead of infinity.
Took 5 seconds.
Good decimal precision with importing decimal module in python.

"""

print(results)

print("Approximate calculated below")
print(str(piN(10000000)))
print("".join('3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610'.split(" ")))
print("Expected Approx for 100 digits of Pi above")
