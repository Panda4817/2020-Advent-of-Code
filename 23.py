def part1(data):
  cups = [int(i) for i in list(data)]
  moves = 100
  decider = 0
  for i in range(moves):
    current = cups[decider]
    begin = decider + 1
    if begin == len(cups):
      begin = 0
    end = decider + 4
    if end >= len(cups):
      end = end - len(cups)
    if end > begin:
      pick_up = cups[begin: end]
    else:
      pick_up = cups[begin:] + cups[0: end]
    destination = current - 1
    if destination < min(cups):
      destination = max(cups)
    while(destination in pick_up):
      destination = destination - 1
      if destination < min(cups):
        destination = max(cups)
    for p in pick_up:
      cups.remove(p)
    index = cups.index(destination)
    cups = cups[:index + 1] + pick_up + cups[index + 1:]
    if cups.index(current) != decider:
      adjust = cups.index(current) - decider
      remove = cups[0:adjust]
      for r in remove:
        cups.remove(r)
      cups = cups + remove
    decider += 1
    if decider == len(cups):
      decider = 0
  index_one = cups.index(1)

  # part 1
  ans = cups[index_one + 1: ] + cups[:index_one]
  return "".join([str(i) for i in ans])

def part2(data):
  data = [2, 1, 9, 7, 4, 8, 3, 6, 5]
  #data = [3, 8, 9, 1, 2, 5, 4, 6, 7]
  mx = max(data)
  cups = {}
  for d in range(9):
      try:
          cups[data[d]] = data[d + 1]
      except IndexError:
          continue
  cups[data[-1]] = mx + 1
  print(cups)
  for i in range(mx + 1, 1000000 + 1):
      cups[i] = i + 1
  cups[1000000] = data[0]
  length = len(cups.keys())
  mx = max(cups.keys())
  mn = min(cups.keys())
  moves = 10000000
  decider = data[0]
  print("running...")
  for i in range(moves):
      current = decider
      one  = cups[decider]
      two = cups[one]
      three = cups[two]
      four = cups[three]
      cups[decider] = four
      destination = current
      while(destination == one or destination == two or destination == three or destination == current):
          destination -= 1
          if destination < mn:
              destination = mx
      nx = cups[destination]
      cups[destination] = one
      cups[one] = two
      cups[two]= three
      cups[three] = nx
      decider = cups[current]

