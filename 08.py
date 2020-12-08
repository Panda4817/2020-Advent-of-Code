import copy

def part1(data):
  lst = data.split("\n")
  instructions = []
  
  for l in lst:
    parts = l.split()
    instructions.append([parts[0], int(parts[1]), 0])

  count = 0
  current = 0
  a = 0

  while(count < 2):
    instructions[current][2] += 1
    count = instructions[current][2]
    if count == 2:
      break
    if instructions[current][0] == 'nop':
      current += 1
    elif instructions[current][0] == 'acc':
      a += instructions[current][1]
      current += 1
    else:
      current += instructions[current][1]
    
  return a

def part2(data):
  lst = data.split("\n")
  instructions = []
  for l in lst:
    parts = l.split()
    instructions.append([parts[0], int(parts[1]), 0])
  
  i = copy.deepcopy(instructions)
  count = 0
  current = 0
  a = 0
  tryNum = 0
  
  while(current < len(i)):
    if current >= len(i):
      break
    
    a = 0
    count = 0
    current = 0
    i.clear()
    i = copy.deepcopy(instructions)
    
    if i[tryNum][0] == 'jmp':
      i[tryNum][0] = 'nop'
    elif i[tryNum][0] == 'nop':
      i[tryNum][0] = 'jmp'
    else:
      tryNum += 1
      continue
    
    while(count < 2 or current < len(i)):
      if current >= len(i):
        break
      i[current][2] += 1
      count = i[current][2]
      if count == 2:
        break
      if i[current][0] == 'nop':
        current += 1
      elif i[current][0] == 'acc':
        a += i[current][1]
        current += 1
      else:
        current += i[current][1]
    
    tryNum += 1
  
  return a
