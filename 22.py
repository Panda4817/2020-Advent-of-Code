import copy

def part1(data):
  lst = data.split("\n\n")
  pl1 = []
  pl2 = []
  for l in lst[0].split("\n"):
    if l == 'Player 1:':
      continue
    pl1.append(int(l))
  for l in lst[1].split("\n"):
    if l == 'Player 2:':
      continue
    pl2.append(int(l))

  while(len(pl1) > 0 and len(pl2) > 0):
    x = pl1.pop(0)
    y = pl2.pop(0)
    if x > y:
      pl1.append(x)
      pl1.append(y)
    elif y > x:
      pl2.append(y)
      pl2.append(x)

  if len(pl1) == 0:
    i = len(pl2)
    winner = pl2
  elif len(pl2) == 0:
    i = len(pl1)
    winner = pl1

  num = 0
  for w in winner:
    num += (w * i)
    i -= 1
  
  return num

def part2(data):
  lst = data.split("\n\n")
  pl1 = []
  pl2 = []
  for l in lst[0].split("\n"):
    if l == 'Player 1:':
      continue
    pl1.append(int(l))
  for l in lst[1].split("\n"):
    if l == 'Player 2:':
      continue
    pl2.append(int(l))

  def recurse(p1, p2):
    print("recurse")
    rnds = {}
    rr = 1
    while(len(p1) > 0 and len(p2) > 0):
      for k, v in rnds.items():
        if p1 == v[1] and p2 == v[2]:
          return 1
      rnds[rr] = {1: copy.deepcopy(p1), 2: copy.deepcopy(p2)}
      x = p1.pop(0)
      y = p2.pop(0)
      if len(p1) >= x and len(p2) >= y:
        answer = recurse(copy.deepcopy(p1[:x]), copy.deepcopy(p2[:y]))
      elif x > y:
        answer = 1  
      elif y > x:
        answer = 2
      if answer == 1:
        p1.append(x)
        p1.append(y)
      elif answer == 2:
        p2.append(y)
        p2.append(x)
      rr += 1
    
    if len(p1) == 0:
      return 2
    elif len(p2) == 0:
      return 1

  
  
  rounds = {}
  r = 1
  winner = None
  while(len(pl1) > 0 and len(pl2) > 0):
    for k, v in rounds.items():
      if pl1 == v[1] and pl2 == v[2]:
        winner = pl1
        break
    if winner != None:
      break
    rounds[r] = {1: copy.deepcopy(pl1), 2: copy.deepcopy(pl2)}
    
    p = pl1.pop(0)
    q = pl2.pop(0)
    
    if len(pl1) >= p and len(pl2) >= q:
      print("\n")
      answer = recurse(copy.deepcopy(pl1[:p]), copy.deepcopy(pl2[:q]))
    elif p > q:
      answer = 1  
    elif q > p:
      answer = 2
    
    if answer == 1:
      pl1.append(p)
      pl1.append(q)
    elif answer == 2:
      pl2.append(q)
      pl2.append(p)
    r += 1
    print(r, pl1, pl2)
    
  
  
  if len(pl1) == 0:
    i = len(pl2)
    winner = pl2
  elif len(pl2) == 0:
    i = len(pl1)
    winner = pl1
  elif winner:
    i = len(pl1)

  num = 0
  for w in winner:
    num += (w * i)
    i -= 1
  
  return num