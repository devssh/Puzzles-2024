





import json

perfect_list = [6, 28, 496, 8128, 33550336]
mersenne_primes = []
summation_perfect = [3, 7, 31, 127, 8191]
search_mersenne_till = 130

actual_list = {
"perfect_numbers": [
6, 28, 496, 8128, 33550336, 8589869056, 137438691328, "230584.......952128"
],
"mersenne_numbers": [
3, 7, 31, 127, 8191, 131071, 524287, 2147483647
]
}


def prime_factors(n):
  factor = [1]
  for i in range(2, n):
    if n % i == 0:
      factor = [*factor, i]
  return {"number": n, "factor": factor, "sum": sum(factor)}

def summation_of(n):
  sum_result = int(n*(n+1)/2)
  return {"mersenne_prime": n, "sum": sum_result}

#replace with pre-populated list of prime numbers to check factors of by a number sieve
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
    print(json.dumps(summation_of(num), indent=4))

  print(json.dumps(perfect_brute, indent=4))

  #summation_of_7th = summation_of(131071)
  #print(json.dumps(summation_of_7th, indent=4))
  #print("it's never gonna factor that far without sieve")
  #print(json.dumps(prime_factors(summation_of_7th["sum"]), indent=4))



