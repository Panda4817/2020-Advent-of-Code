import copy

def part1(data):
  cubes = data.split("\n")
  cycles = 6
  c = {}
  z = 0
  for y in range(len(cubes)):
    for x in range(len(cubes[y])):
      c[(x, y, z)] = cubes[y][x]
  print(c)

  def find_neighbores(cube):
    arr = []
    for z in range(cube[2] - 1, cube[2] + 2):
      for y in range(cube[1] - 1, cube[1] + 2):
        for x in range(cube[0] - 1, cube[0] + 2):
          if (x, y, z) != cube:
            arr.append((x, y, z))
    return arr

  for i in range(cycles):
    dic = copy.deepcopy(c)
    for k, v in dic.items():
      neighbores = find_neighbores(k)
      for n in neighbores:
        if n not in c.keys():
          c[n] = '.'
    
    dic = copy.deepcopy(c)
    for k, v in dic.items():
      neighbores = find_neighbores(k)
      count = 0
      for n in neighbores:
        try:
          if dic[n] == '#':
            count += 1
        except KeyError:
          continue
      if v == '#':
        if count == 2 or count == 3:
          c[k] = '#'
        else:
          c[k] = '.'
      else:
        if count == 3:
          c[k] = '#'
        else:
          c[k] = '.'
  
  num = 0
  for v in c.values():
    if v == '#':
      num += 1
  return num

def part2(data):
  cubes = data.split("\n")
  cycles = 6
  c = {}
  z = 0
  w = 0
  for y in range(len(cubes)):
    for x in range(len(cubes[y])):
      c[(x, y, z, w)] = cubes[y][x]
  print(c)

  def find_neighbores(cube):
    arr = []
    for w in range(cube[3] - 1, cube[3] + 2):
      for z in range(cube[2] - 1, cube[2] + 2):
        for y in range(cube[1] - 1, cube[1] + 2):
          for x in range(cube[0] - 1, cube[0] + 2):
            if (x, y, z, w) != cube:
              arr.append((x, y, z, w))
    return arr

  for i in range(cycles):
    dic = copy.deepcopy(c)
    for k, v in dic.items():
      neighbores = find_neighbores(k)
      for n in neighbores:
        if n not in c.keys():
          c[n] = '.'
    
    dic = copy.deepcopy(c)
    for k, v in dic.items():
      neighbores = find_neighbores(k)
      count = 0
      for n in neighbores:
        try:
          if dic[n] == '#':
            count += 1
        except KeyError:
          continue
      if v == '#':
        if count == 2 or count == 3:
          c[k] = '#'
        else:
          c[k] = '.'
      else:
        if count == 3:
          c[k] = '#'
        else:
          c[k] = '.'
  
  num = 0
  for v in c.values():
    if v == '#':
      num += 1
  return num
