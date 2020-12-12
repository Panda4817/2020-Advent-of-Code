def part1(data):
  nav = data.split("\n")
  n = 'N'
  s = 'S'
  w = 'W'
  e = 'E'
  f = 'F'
  r = 'R'
  l = 'L'
  current_face = e
  n_s_val = 0
  e_w_val = 0
  rotate = 0

  for d in nav:
    val = int(d[1:])

    if d[0] == f:
      if current_face == e:
        e_w_val += val
      elif current_face == w:
        e_w_val -= val
      elif current_face == n:
        n_s_val += val
      elif current_face == s:
        n_s_val -= val
    
    elif d[0] == e:
      e_w_val += val
    
    elif d[0] == w:
      e_w_val -= val
    
    elif d[0] == n:
      n_s_val += val
    
    elif d[0] == s:
      n_s_val -= val
    
    elif d[0] == r:
      rotate += val
    
    elif d[0] == l:
      rotate -= val
    
    rotate = rotate % 360
    if (rotate == 90) or (rotate == -270):
      current_face = s
    elif (rotate == 180) or (rotate == -180):
      current_face = w
    elif (rotate == 270) or (rotate == -90):
      current_face = n
    else:
      current_face = e

  return abs(e_w_val) + abs(n_s_val)

def part2(data):
  nav = data.split("\n")
  n = 'N'
  s = 'S'
  w = 'W'
  e = 'E'
  f = 'F'
  r = 'R'
  l = 'L'
  way_e_val = 10
  way_n_val = 1
  n_s_val = 0
  e_w_val = 0

  for d in nav:
    val = int(d[1:])
    if d[0] == e:
      way_e_val += val
    
    elif d[0] == w:
      way_e_val -= val
    
    elif d[0] == n:
      way_n_val += val
    
    elif d[0] == s:
      way_n_val -= val
    
    elif d[0] == f:
      temp_e = val * way_e_val
      temp_n = val * way_n_val
      n_s_val += temp_n
      e_w_val += temp_e
    
    elif d[0] == r:
      if val == 90:
        temp_e = way_n_val
        temp_n = -way_e_val
        way_e_val = temp_e
        way_n_val = temp_n
      elif val == 180:
        temp_e = -way_e_val
        temp_n = -way_n_val
        way_e_val = temp_e
        way_n_val = temp_n
      elif val == 270:
        temp_e = -way_n_val
        temp_n = way_e_val
        way_e_val = temp_e
        way_n_val = temp_n
    
    elif d[0] == l:
      if val == 90:
        temp_e = -way_n_val
        temp_n = way_e_val
        way_e_val = temp_e
        way_n_val = temp_n
      elif val == 180:
        temp_e = -way_e_val
        temp_n = -way_n_val
        way_e_val = temp_e
        way_n_val = temp_n
      elif val == 270:
        temp_e = way_n_val
        temp_n = -way_e_val
        way_e_val = temp_e
        way_n_val = temp_n
    
  return abs(e_w_val) + abs(n_s_val)
    

