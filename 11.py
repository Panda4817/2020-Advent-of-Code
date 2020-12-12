def part1(data):
  seats = data.split("\n")
  
  def check(y, x, h, w):
    if y < 0 or y >= h:
      return False
    elif x < 0 or x >= w:
      return False
    return True
  
  def get_adj(y, x):
    neighbores = []
    neighbores.append((y - 1, x))
    neighbores.append((y + 1, x))
    neighbores.append((y, x - 1))
    neighbores.append((y, x + 1))
    neighbores.append((y - 1, x - 1))
    neighbores.append((y - 1, x + 1))
    neighbores.append((y + 1, x - 1))
    neighbores.append((y + 1, x + 1))
    return neighbores

  changed = True
  while (changed == True):
    new_plan = []
    taken = 0
    for s in range(len(seats)):
      row = ''
      for r in range(len(seats[s])):
        if seats[s][r] == '.':
          row += '.'
          continue
        num = 0
        neighbores = get_adj(s, r)
        for n in neighbores:
          if check(n[0], n[1], len(seats), len(seats[s])) == False:
            continue
          if seats[n[0]][n[1]] == '#':
            num += 1
        if num == 0 and seats[s][r] == 'L':
          row += '#'
          taken += 1
        elif num >= 4 and seats[s][r] == '#':
          row += 'L'
        else:
          if seats[s][r] == '#':
            taken += 1
          row += seats[s][r]
      new_plan.append(row)
    if new_plan == seats:
      changed = False
      break
    else:
      seats.clear()
      seats.extend(new_plan)
  
  return taken

def part2(data):
  seats = data.split("\n")

  def check(y, x, h, w):
    if y < 0 or y >= h:
      return False
    elif x < 0 or x >= w:
      return False
    return True
  
  def get_num_taken_seats(y, x, h, w, seats):
    num = 0
    for i in range(1, h):
      temp_y = y - i
      if check(temp_y, x, h, w):
        if seats[temp_y][x] == '#' or seats[temp_y][x] == 'L':
          if seats[temp_y][x] == '#':
            num += 1
          break
      else:
        break
    
    for i in range(1, h):
      temp_y = y + i
      if check(temp_y, x, h, w):
        if seats[temp_y][x] == '#' or seats[temp_y][x] == 'L':
          if seats[temp_y][x] == '#':
            num += 1
          break
      else: break
    
    for i in range(1, w):
      temp_x = x - i
      if check(y, temp_x, h, w):
        if seats[y][temp_x] == '#' or seats[y][temp_x] == 'L':
          if seats[y][temp_x] == '#':
            num += 1
          break
      else: break
    
    for i in range(1, w):
      temp_x = x + i
      if check(y, temp_x, h, w):
        if seats[y][temp_x] == '#' or seats[y][temp_x] == 'L':
          if seats[y][temp_x] == '#':
            num += 1
          break
      else: break
    
    x_minus = 1
    for i in range(1, h):
      temp_y = y - i
      temp_x = x - x_minus
      if check(temp_y, temp_x, h, w):
        if seats[temp_y][temp_x] == '#' or seats[temp_y][temp_x] == 'L':
          if seats[temp_y][temp_x] == '#':
            num += 1
          break
      else: break
      x_minus += 1
    
    x_plus = 1
    for i in range(1, h):
      temp_y = y - i
      temp_x = x + x_plus
      if check(temp_y, temp_x, h, w):
        if seats[temp_y][temp_x] == '#' or seats[temp_y][temp_x] == 'L':
          if seats[temp_y][temp_x] == '#':
            num += 1
          break
      else: break
      x_plus += 1
    
    x_plus = 1
    for i in range(1, h):
      temp_y = y + i
      temp_x = x + x_plus
      if check(temp_y, temp_x, h, w):
        if seats[temp_y][temp_x] == '#' or seats[temp_y][temp_x] == 'L':
          if seats[temp_y][temp_x] == '#':
            num += 1
          break
      else: break
      x_plus += 1
  
    x_minus = 1
    for i in range(1, h):
      temp_y = y + i
      temp_x = x - x_minus
      if check(temp_y, temp_x, h, w):
        if seats[temp_y][temp_x] == '#' or seats[temp_y][temp_x] == 'L':
          if seats[temp_y][temp_x] == '#':
            num += 1
          break
      else: break
      x_minus += 1

    return num
  
  changed = True
  while (changed == True):
    new_plan = []
    taken = 0
    for s in range(len(seats)):
      row = ''
      for r in range(len(seats[s])):
        if seats[s][r] == '.':
          row += '.'
          continue
        num = get_num_taken_seats(s, r, len(seats), len(seats[s]), seats)
        if num == 0 and seats[s][r] == 'L':
          row += '#'
          taken += 1
        elif num >= 5 and seats[s][r] == '#':
          row += 'L'
        else:
          if seats[s][r] == '#':
            taken += 1
          row += seats[s][r]
      new_plan.append(row)
    if new_plan == seats:
      changed = False
      break
    else:
      seats.clear()
      seats.extend(new_plan)
  
  return taken


  
  

  
      
          

    
