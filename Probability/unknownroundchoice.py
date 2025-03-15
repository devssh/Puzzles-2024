

import numpy as np


already_seen = 32
print(f"Already seen {already_seen}")
seen = [x for x in range(already_seen)]
window_size = 5

def choose(total_choices):
  return list(np.random.choice(total_choices, window_size))

def keep_rolling(total_choices):
  global seen
  new_seen = choose(total_choices)
  seen = list(set([*seen, *new_seen]))


def get_seen():
  total_choices = already_seen + np.random.randint(1968)
  # unknown total coupons, between 32 and 2000
  for x in range(100):
    keep_rolling(total_choices)
  return [len(seen), total_choices]

trials = 10000
seen_frequency = {}
cumulative = 0

for i in range(trials):
  [seen_count, total_choices] = get_seen()
  if total_choices in seen_frequency.keys():
    seen_frequency[total_choices] = [*seen_frequency[total_choices], seen_count]
  else:
    seen_frequency[total_choices] = [seen_count]
  seen = [x for x in range(already_seen)]

print(f"100 rounds, unknown {total_choices} choices, observed coupons seen")
for x in list(sorted(seen_frequency.keys())):
  count = round(sum(seen_frequency[x]) / len(seen_frequency[x]), 2)
  print(f"100 rounds, {str(count).zfill(6)} coupons seen, Actual coupon count: {str(x).zfill(3)}")

print("Coupons seen -> Probability through Maximum Likelihood Estimation of prior probabilities")

