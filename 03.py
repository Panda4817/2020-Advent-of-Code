def part1(data):
  lst = list(data.split("\n"))
  count = 0
  along = 3
  for r in range(1, len(lst)):
    s = lst[r]
    while(along > len(s)-1):
      s += lst[r]
    if s[along] == '#':
      count += 1
    along += 3
  return count

def part2(data):
  lst = list(data.split("\n"))
  increase_by = [1, 5, 7, 1]
  along = [1, 5, 7, 1]
  count = [0, 0, 0, 0]
  for a in range(len(along)):
    if a == 3:
      for r in range(2, len(lst)):
        if r % 2 == 0:
          s = lst[r]
          while(along[a] > len(s)-1):
            s += lst[r]
          if s[along[a]] == '#':
            count[a] += 1
          along[a] += increase_by[a]
    else:
      for r in range(1, len(lst)):
        s = lst[r]
        while(along[a] > len(s)-1):
          s += lst[r]
        if s[along[a]] == '#':
          count[a] += 1
        along[a] += increase_by[a]

  return count[0]*count[1]*count[2]*count[3]*193
