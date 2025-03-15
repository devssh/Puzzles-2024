

import numpy as np


already_seen = 32
#seen = []
seen = [x for x in range(already_seen)]
history = []
total_choices = 100
window_size = 5

def choose():
  return list(np.random.choice(total_choices, window_size))


def keep_rolling():
  global seen
  global history
  new_seen = choose()
  seen = list(set([*new_seen, *seen]))
  history = [*history, new_seen]


def print_rounds():
  while(len(seen) < total_choices*99/100):
    keep_rolling()
  #print(str(len(history)) + " rounds taken")
  #for x in history:
  #  print(x)
  return len(history)

trials = 10000
rounds = []
cumulative = 0

for i in range(trials):
  rounds_taken = print_rounds()
  rounds = [*rounds, rounds_taken]
  #seen = []
  seen = [x for x in range(already_seen)]
  history = []

print(f"Choosing {window_size} choices every round till all {total_choices} choices are seen")
for x in list(sorted(list(set(rounds)))):
  count = len([y for y in rounds if y==x])
  percentage = count*100/trials
  cumulative = cumulative + percentage
  print(f"{str(x).zfill(3)} rounds: {str(count).zfill(3)} times, Percentage:{str(round(percentage, 1)).zfill(5)}% Cumulative:{str(round(cumulative, 2)).zfill(5)}%")

