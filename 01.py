def part1(data):
  __import__('time').sleep(1)
  # Data is automatically read from 01.txt
  strings = list(data.split("\n"))
  num = [int(item) for item in strings]
  target = 2020
  num1 = 0
  num2 = 0
  for n in range(0, len(num) - 1):
    for m in range(n + 1, len(num) - 1):
      if ((num[n] + num[m]) == target) and (n != m):
        num1 = num[n]
        num2 = num[m]
        print(num1, num2)
  return num1 * num2

def part2(data):
  __import__('time').sleep(1)
  # Data is automatically read from 01.txt
  strings = list(data.split("\n"))
  num = [int(item) for item in strings]
  target = 2020
  num1 = 0
  num2 = 0
  num3 = 0
  for n in range(0, len(num) - 1):
    for m in range(n + 1, len(num) - 1):
      for p in range(m + 1, len(num) - 1):
        if ((num[n] + num[m] + num[p]) == target) and (n != m != p):
          num1 = num[n]
          num2 = num[m]
          num3 = num[p]
          print(num1, num2, num3)
  return num1 * num2 * num3