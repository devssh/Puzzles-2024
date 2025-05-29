





import json

perfect_list = [6, 28, 496, 8128]
mersenne_primes = []
summation_perfect = [3, 7, 31, 127]


def prime_factors(n):
  factor = [1]
  for i in range(2, n):
    if n % i == 0:
      factor = [*factor, i]
  return {"number": n, "factor": factor, "sum": sum(factor)}

def summation_of(n):
  sum_result = n*(n+1)/2
  return {"mersenne_prime": n, "sum": sum_result}


if __name__ == "__main__":
  for num in perfect_list:
    print(json.dumps(prime_factors(num), indent=4))
  
  for num in summation_perfect:
    print(json.dumps(summation_of(num)))







