from math import prod

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
  
  b = [i for i in range(0, length) if buses[i] != 'x']
  print(b)
  n = [buses[j] for j in range(0, length) if buses[j] != 'x']
  print(n)
  lg = len(n)
  N_prod = prod(n)

  N = [N_prod // mod for mod in n]


  x = []
  for l in range(lg):
    z = N[l] % n[l]
    y = pow(z, -1, n[l])
    x.append(y)
    

  
  prod_up = [b[m] * N[m] * x[m] for m in range(lg)]
  t = (sum(prod_up)) #% N_prod

  for bus in n:
    print(t % bus)

  


  
  #found = False
  #t = buses[0]
  #t = 100005097993714
  #while (t % buses[0] != 0):
    #t += 1

  #while (found == False):  
    #found = True
    #for b in range(1, length):
      #if buses[b] == 'x':
        #ontinue
      #temp = t + b
      #if temp % buses[b] != 0:
        #print(t)
        #found = False
        #break
    #if found == True:
      #break
    #t += buses[0]

  return t