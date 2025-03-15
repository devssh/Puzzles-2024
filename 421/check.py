



upper_limit = 101_000_000

def read_lower_limit():
  with open("data.txt", "r") as f:
    return int("\n".join(f.readlines()).strip())

lower_limit = read_lower_limit()

def write_to_file():
  with open("data.txt", "w") as f:
    f.writelines(f"\n\n\n\n\n {upper_limit:_}")
    f.close()

stop_list = [4, 2, 1]
maximum = lower_limit

def check_number(number):
  global maximum
  maximum = max(maximum, number)
  if number in stop_list:
    return True
  if number < lower_limit: 
    return True
  if (number % 2) == 0:
    return check_number(int(number/2));
  return check_number(3*number + 1)
  

def run():
  global lower_limit
  print("Lower limit is " + str(lower_limit))
  if lower_limit >= upper_limit:
    print("Limit reached")
  for number in range(lower_limit, upper_limit):
    outcome = check_number(number)
    if not outcome:
      print("found an invalid number " + str(number))
      break
    lower_limit = number
  print("Done")
  write_to_file()
  print("Maximum: " + str(maximum))
  
if __name__ == "__main__":
  run()
