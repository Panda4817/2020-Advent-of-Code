from math import prod
#from functools import reduce

def part1(data):
  lst = data.split("\n")
  earliest = int(lst[0])
  buses = [int(b) for b in lst[1].split(",") if b != 'x']
  number_lines = []

  for b in buses:
    num = 0
    arr = [0]
    while (num < earliest):
      num += b
      arr.append(num)
    arr.reverse()
    number_lines.append(arr)
  
  diff = float('inf') 
  current = 0
  for n in number_lines:
    temp = n[0] - earliest
    if temp < diff:
      diff = temp
      current = buses[number_lines.index(n)]
  
  return diff * current

def part2(data):
  # Using Chinese Remainder Theorem to solve this
  lst = data.split("\n")
  buses = [int(b) if b != 'x' else b for b in lst[1].split(",")]
  length = len(buses)
  
  offsetts = [i for i in range(0, length) if buses[i] != 'x']
  print(offsetts)
  moduli = [buses[j] for j in range(0, length) if buses[j] != 'x']
  print(moduli)
  
  # My own code for chinese remainder theorem
  lg = len(moduli)
  remainders = []
  for l in range(lg):
    remainders.append(moduli[l] - offsetts[l])
  
  print(remainders)
  N_prod = prod(moduli)
  
  N = [(N_prod // mod) for mod in moduli]
  print(N)
  x = []
  for l in range(lg):
    z = pow(N[l], -1 , moduli[l])
    x.append(z)
    # z = N[l] % moduli[l]
    # if z == 1:
    #   x.append(1)
    #   continue
    # a = 0
    # while (a != 1):
    #   y += 1
    #   a = (z * y) % moduli[l]
    # print(x)
    # x.append(y)

  print(x)
  prod_up = [(remainders[m] * N[m] * x[m]) for m in range(lg)]
    

  t = (sum(prod_up)) % N_prod
  print(t)
  
  """
  # Brute Force
  
  found = False
  t = buses[0]
  t = 100005097993714
  while (t % buses[0] != 0):
    t += 1

  while (found == False):  
    found = True
    for b in range(1, length):
      if buses[b] == 'x':
        ontinue
      temp = t + b
      if temp % buses[b] != 0:
        print(t)
        found = False
        break
    if found == True:
      break
    t += buses[0]

  # Rosetta Code
  def chinese_remainder(n, a):
      sum = 0
      prod = reduce(lambda a, b: a*b, n)
      for n_i, a_i in zip(n, a):
          p = prod // n_i
          sum += a_i * mul_inv(p, n_i) * p
      return sum % prod
  
  def mul_inv(a, b):
      b0 = b
      x0, x1 = 0, 1
      if b == 1: return 1
      while a > 1:
          q = a // b
          a, b = b, a%b
          x0, x1 = x1 - q * x0, x0
      if x1 < 0: x1 += b0
      return x1
  
  t = chinese_remainder(n, b)
  """
  for bus,r in zip(moduli,remainders):
    print(t % bus)

  return t