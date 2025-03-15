


import sys
sys.setrecursionlimit(100000)

random_number = 731904283549923109231875438214321812490908534243913215986359183210983219020192359
random_number = random_number * 574690951604920310642351063142539

def write_file(string):
  with open("bigrandomcollatzseq.txt", "w") as f:
    f.writelines(string)
    f.close()

stop_list = [4, 2, 1]
def reduce_count(number, sequence):
  if number in stop_list:
    return [*sequence, *stop_list]
  if (number%2) == 0:
    return reduce_count(int(number//2), [*sequence, int(number//2)])
  if (number%2) == 1:
    return reduce_count(number*3 + 1, [*sequence, number*3 + 1])
  

if __name__ == "__main__":
  print(f"Random: {random_number:_}")
  output = reduce_count(random_number, [random_number])
  print(len(output))
  random_output = "".join([str(x) for x in output])[::-1]
  print(random_output)
  write_file(random_output)


