def part1(data):
  lst = data.split("\n")
  
  highest = 0

  for p in lst:
    rows = []
    for r in range(128):
      rows.append(r)
    
    columns = []
    for c in range(8):
      columns.append(c)
    
    row = p[:7]
    column = p[7:]
    
    for r in row:
      half = len(rows) // 2
      if r == 'F': keep = rows[:half]
      else: keep = rows[half:]
      rows = keep
    
    for c in column:
      half = len(columns) // 2
      if c == 'L': keep = columns[:half]
      else: keep = columns[half:]
      columns = keep
    
    id_num = (rows[0] * 8) + columns[0]
    if id_num > highest: highest = id_num

  return highest

def part2(data):
  lst = data.split("\n")
  seats = {}
  for r in range(128):
    seats[r] = [0, 0, 0, 0, 0, 0, 0, 0]
  
  for p in lst:
    rows = []
    for r in range(128):
      rows.append(r)
    
    columns = []
    for c in range(8):
      columns.append(c)
    
    row = p[:7]
    column = p[7:]
    
    for r in row:
      half = len(rows) // 2
      if r == 'F': keep = rows[:half]
      else: keep = rows[half:]
      rows = keep
    
    for c in column:
      half = len(columns) // 2
      if c == 'L': keep = columns[:half]
      else: keep = columns[half:]
      columns = keep
    
    id_num = (rows[0] * 8) + columns[0]
    seats[rows[0]][columns[0]] = id_num

  for k, v in seats.items():
    for c in v:
       if c == 0 and v[v.index(c)-1] != 0 and v[v.index(c)+1] != 0:
         return k * 8 + v.index(c)

  return
