





import json

perfect_list = [6, 28, 496, 8128]
mersenne_primes = []
summation_perfect = [3, 7, 31, 127]
search_mersenne_till = 500

def prime_factors(n):
  factor = [1]
  for i in range(2, n):
    if n % i == 0:
      factor = [*factor, i]
  return {"number": n, "factor": factor, "sum": sum(factor)}

def summation_of(n):
  sum_result = int(n*(n+1)/2)
  return {"mersenne_prime": n, "sum": sum_result}

def brute_search():
  results = {"perfect_numbers": [], "mersenne_number": []}
  for i in range(2, search_mersenne_till):
    summation_result = summation_of(i)
    pf_results = prime_factors(summation_result["sum"])
    if pf_results["sum"] == pf_results["number"]:
      results["perfect_numbers"] = [*results["perfect_numbers"], pf_results["sum"]]
      results["mersenne_number"] = [*results["mersenne_number"], i]
  return results

perfect_brute = brute_search()

if __name__ == "__main__":
  for num in perfect_list:
    print(json.dumps(prime_factors(num), indent=4))
  
  for num in summation_perfect:
    print(json.dumps(summation_of(num)))

  print(json.dumps(perfect_brute))






