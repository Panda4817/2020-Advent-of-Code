import itertools

def part1(data):
  lst = data.split("\n")
  mem = {}
  current_mask = ""
  for l in lst:
    if l[0:4] == 'mask':
      current_mask = l[7:len(l)]
    else:
      parts = l.split(" = ")
      key = parts[0][4:-1]
      num = int(parts[1])
      mem[key] = num
      binary = bin(num)[2:]
      r = len(current_mask) - len(binary)
      extra = ''
      for i in range(r):
        extra += '0'
      current_val = extra + binary
      new_val = ''
      for i in range(36):
        if current_mask[i] == 'X':
          new_val += current_val[i]
        else:
          new_val += current_mask[i]
      new_val_int = int(new_val, 2)
      mem[key] = new_val_int
  
  return sum(mem.values())

def part2(data):
  lst = data.split("\n")
  mem = {}
  current_mask = ""
  for l in lst:
    if l[0:4] == 'mask':
      current_mask = l[7:len(l)]
    else:
      parts = l.split(" = ")
      key = int(parts[0][4:-1])
      num = int(parts[1])
      binary = bin(key)[2:]
      r = len(current_mask) - len(binary)
      extra = ''
      for i in range(r):
        extra += '0'
      current_val = extra + binary
      new_val = ''
      x_added = 0
      for i in range(36):
        if current_mask[i] == 'X':
          new_val += 'X'
          x_added += 1
        elif current_mask[i] == '1':
          new_val += '1'
        else:
          new_val += current_val[i]
      if x_added == 0:
        mem[int(new_val, 2)] = num
        continue
      floats = []
      combi = list(itertools.product([0, 1], repeat=x_added))
      for i in range(len(combi)):
        temp = ''
        added = 0
        for j in new_val:
          if j == 'X':
            temp += str(combi[i][added])
            if (added != x_added - 1):
              added += 1
          else:
            temp += j
        floats.append(temp)
      for f in floats:
         mem[int(f, 2)] = num

  return sum(mem.values())