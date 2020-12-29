import copy
# Part 1 and 2 in same function
def part1(data):
  intructions = data.split("\n")
  joined = [
    's', 'n'
  ]
  seperate = [
    'e', 'w'
  ]
  parsed = []
  for i in intructions:
    print(i)
    p = []
    for c in range(len(i)):
      prev = c - 1
      nex = c + 1
      if prev < 0 and i[c] in seperate:
        p.append(i[c])
      elif i[c] in seperate and i[prev] not in joined:
        p.append(i[c])
      elif i[c] in joined and i[nex] in seperate:
        p.append(i[c] + i[nex])
    parsed.append(p)

  tiles = {}
  start = (0, 0)
  for instruction in parsed:
    current = list(start)
    for p in instruction:
      if p == 'w':
        current[0] -= 2
      elif p == 'e':
        current[0] += 2
      elif p == 'nw':
        current[0] -= 1
        current[1] += 1
      elif p == 'se':
        current[0] += 1
        current[1] -= 1
      elif p == 'ne':
        current[0] += 1
        current[1] += 1
      elif p == 'sw':
        current[0] -= 1
        current[1] -= 1
    t = tuple(current)
    if t in tiles:
      if tiles[t] == 0:
        tiles[t] = 1
      elif tiles[t] == 1:
        tiles[t] = 0
    else:
      tiles[t] = 1
  
  # Part 1
  vals = [v for v in tiles.values()]
  ans = vals.count(1)
  
  days = 100

  def get_nbs(tile):
    n = [
      (tile[0] - 2, tile[1]),
      (tile[0] + 2, tile[1]),
      (tile[0] - 1, tile[1] + 1),
      (tile[0] + 1, tile[1] - 1),
      (tile[0] + 1, tile[1] + 1),
      (tile[0] - 1, tile[1] - 1)
    ]
    return n

  for i in range(days):
    cp_tiles = copy.deepcopy(tiles)
    for t in tiles:
      neighbors = get_nbs(t)
      for n in neighbors:
        if n not in tiles:
          cp_tiles[n] = 0
    for t, v in cp_tiles.items():
      neighbors = get_nbs(t)
      how_many_black = 0
      for n in neighbors:
        if n in cp_tiles:
          if cp_tiles[n] == 1:
            how_many_black += 1
      
      if v == 1 and (how_many_black == 0 or how_many_black > 2):
        tiles[t] = 0
      elif v == 0 and how_many_black == 2:
        tiles[t] = 1
  
  # Part 2
  vals = [v for v in tiles.values()]
  ans2 = vals.count(1)

  return ans, ans2

    


