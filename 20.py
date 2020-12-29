import numpy as np
import math
import copy
# Part 1 and 2 in the same function
class Edge(object):

  def __init__(self, data):
    self.data = data
  
  def __eq__(self, other):
    if self.data == other.data or self.data == tuple(i for i in reversed(other.data)):
      return True
    else:
      return False
  
  def __hash__(self):
    h1 = hash(self.data)
    r = tuple(i for i in reversed(self.data))
    h2 = hash(r)
    return h1 + h2


class Tile(object):

  def __init__(self, _id, data):
    self._id = _id
    self.data = data
    self.placed = False
  
  def __eq__(self, other):
    return self.id == other.id
  
  def __str__(self):
    s = f'Tile {self.id}:\n'
    for row in self.data:
      s += ''.join([str(col) for col in row]) + '\n'
    return s

  slices = {
    'left': [0,10,0,1],
    'right': [0,10,-1,10],
    'up': [0,1,0,10],
    'down': [-1,10,0,10]
  }

  @property
  def id(self):
    return self._id

  def _edge(self, sl, lr=True):
    d = self.data[
      sl[0]:sl[1],
      sl[2]:sl[3],
    ]

    if lr:
      d = tuple(i[0] for i in d)
    else:
      d = tuple(d[0])
    
    return Edge(d)

  @property
  def edge_top(self):
    sl = self.slices["up"]
    return self._edge(sl, lr=False)
  
  @property
  def edge_bottom(self):
    sl = self.slices["down"]
    return self._edge(sl, lr=False)

  @property
  def edge_left(self):
    sl = self.slices["left"]
    return self._edge(sl, lr=True)
  
  @property
  def edge_right(self):
    sl = self.slices["right"]
    return self._edge(sl, lr=True)
  
  @property
  def edges(self):
    return [
      self.edge_top,
      self.edge_bottom,
      self.edge_left,
      self.edge_right,
    ]
  
  def rotate90(self):
    self.data = np.rot90(self.data)
  
  def fliplr(self):
    self.data = np.fliplr(self.data)
  
  def flipud(self):
    self.data = np.flipud(self.data)

def part1(data):
  initial = data.split("\n\n")
  tiles = []
  for i in initial:
    lines = i.split("\n")
    arr = []
    for l in range(len(lines)):
      if l == 0:
        parts = lines[l].split()
        _id = int(parts[1].split(":")[0])
      else:
        lst = list(lines[l])
        arr.append(lst)
    if arr:
      nplist = np.array(arr)
      numlist = np.where(nplist == '#', 1, 0)
      tiles.append(Tile(_id, numlist))
  
  # Set up for final numpy array
  sides = int(math.sqrt(len(tiles)))
  total = sides*10
  final = np.zeros((total, total), dtype=int)
  ids_np = np.empty((sides, sides), dtype=object)
  ids = np.zeros((sides, sides), dtype=int)
  
  all_slices = {'corners':[], 'edges':[], 'middle':[]}
  slices = []
  # Get all slices
  for i in range(0, total, 10):
    for j in range(0, total, 10):
      sl = [i, 10 + i, j, 10 + j]
      slices.append(sl)
      if sl == [0,10,0,10] or sl == [0,10,total-10,total] or sl == [total-10, total, 0, 10] or sl == [total-10, total, total-10, total]:
        all_slices['corners'].append(sl)
      elif (sl[0] == 0 and sl[1] == 10 and sl[2] >= 0 and sl[2] < total) or (sl[0] == total - 10 and sl[1] == total and sl[2] >= 0 and sl[2] < total) or (sl[2] == 0 and sl[3] == 10 and sl[0] >= 0 and sl[0] < total) or (sl[2] == total - 10 and sl[3] == total and sl[0] >= 0 and sl[0] < total):
        all_slices['edges'].append(sl)
      else:
        all_slices['middle'].append(sl)
  
  # Get all edges
  edges = {}
  for t in tiles:
    for e in t.edges:
      edges.setdefault(e, 0)
      edges[e] += 1
  
  # Get all outer edges
  outer_edges = [k for k, v in edges.items() if v % 2 != 0]
  print(len(outer_edges))
  corner_tiles = []
  edge_tiles = []
  middle_tiles = []

  for t in tiles:
    num_outer_edges = 0
    for e in t.edges:
      if e in outer_edges:
        num_outer_edges += 1
    if num_outer_edges == 2:
      corner_tiles.append(t)
    elif num_outer_edges == 1:
      edge_tiles.append(t)
    else:
      middle_tiles.append(t)

  print(len(corner_tiles), len(edge_tiles), len(middle_tiles))
 
  def get_neighbores(s):
    n = {}

    try:
      n['up'] = ids_np[s[0]-1:s[1]-1, s[2]:s[3]][0][0]
    except IndexError:
      n['up'] = None

    try:
      n['bottom'] = ids_np[s[0]+1:s[1]+1, s[2]:s[3]][0][0]
    except IndexError:
      n['bottom'] = None

    try:
      n['left'] = ids_np[s[0]:s[1], s[2]-1:s[3]-1][0][0]
    except IndexError:
      n['left'] = None

    try:
      n['right'] = ids_np[s[0]:s[1], s[2]+1:s[3]+1][0][0]
    except IndexError:
      n['right'] = None

    return n


  while(0 in ids):
    for s in slices:
      if ids[s[0]//10:s[1]//10,s[2]//10:s[3]//10][0][0] != 0:
        continue
      
      for t in tiles:
        if t.placed == True:
          continue
        found = False
        num_rotated = 0

        n = get_neighbores([s[0]//10,s[1]//10,s[2]//10,s[3]//10])
        while(found == False):
          count = 0
          length = 0
          
          
          
          if n['up']:
            length += 1
            if t.edge_top.data == n['up'].edge_bottom.data:
              count += 1
          if n['bottom']:
            length += 1
            if t.edge_bottom.data == n['bottom'].edge_top.data:
              count += 1
          if n['left']:
            length += 1
            if t.edge_left.data == n['left'].edge_right.data:
              count += 1
          if n['right']:
            length += 1
            if t.edge_right.data == n['right'].edge_left.data:
              count += 1
          
          if s in all_slices['corners']:
            length += 2
            if s == [0,10,0,10]:
              if t.edge_top in outer_edges and t.edge_left in outer_edges:
                count += 2
            elif s == [0,10,total - 10,total]:
              if t.edge_top in outer_edges and t.edge_right in outer_edges:
                count += 2
            elif s == [total - 10, total, 0, 10]:
              if t.edge_bottom in outer_edges and t.edge_left in outer_edges:
                count += 2
            elif s == [total-10, total, total-10, total]:
              if t.edge_bottom in outer_edges and t.edge_right in outer_edges:
                count += 2
          
          elif s in all_slices['edges']:
            length += 1
            if s[0] == 0 and s[1] == 10 and s[2] >= 0 and s[2] < total:
              if t.edge_top in outer_edges:
                count += 1
            elif s[0] == total - 10 and s[1] == total and s[2] >= 0 and s[2] < total:
              if t.edge_bottom in outer_edges:
                count += 1
            elif s[2] == 0 and s[3] == 10 and s[0] >= 0 and s[0] < total:
              if t.edge_left in outer_edges:
                count += 1
            elif s[2] == total - 10 and s[3] == total and s[0] >= 0 and s[0] < total:
              if t.edge_right in outer_edges:
                count += 1

          if length > 0:
            if s in all_slices['corners'] and t in corner_tiles and count == length:
              found = True
            elif s in all_slices['edges'] and t in edge_tiles and count == length:
              found = True
            elif s in all_slices['middle'] and t in middle_tiles and count == length:
              found = True

          if found:
            final[s[0]:s[1],s[2]:s[3]] = t.data
            ids_np[s[0]//10:s[1]//10,s[2]//10:s[3]//10] = t
            ids[s[0]//10:s[1]//10,s[2]//10:s[3]//10] = t.id
            t.placed = True
            break
          

          t.rotate90()
          num_rotated += 1
          if num_rotated == 4:
            t.fliplr()
          if num_rotated == 8:
            t.fliplr()
            t.flipud()
          if num_rotated == 12:
            t.flipud()
            t.fliplr()
            t.flipud()
          if num_rotated == 16:
            t.flipud()
            t.fliplr()
            t.flipud()
            t.fliplr()
          if num_rotated == 20:
            break
        if found:
          break


  print(final)
  print(ids)
  
  num = 1
  for c in all_slices['corners']:
    num *= ids[c[0]//10:c[1]//10,c[2]//10:c[3]//10][0][0]
  

  image_slices = []
  # Get all slices
  for i in range(0, total - sides*2, 8):
    for j in range(0, total - sides*2, 8):
      sl = [i, 8 + i, j, 8 + j]
      image_slices.append(sl)

  image = np.zeros((total - sides*2, total - sides*2), dtype=int)
  for s, i in zip(slices, image_slices):
    a = final[s[0] + 1:s[1] - 1, s[2] + 1:s[3] - 1]
    image[i[0]:i[1], i[2]:i[3]] = a
  
  print(image)

  def pattern_check(i, j, arr):
    try:
      if arr[i + 1: i + 2, j + 1: j + 2] != 1:
        return False
      if arr[i + 1: i + 2, j + 4: j + 5] != 1:
        return False
      if arr[i: i + 1, j + 5: j + 6] != 1:
        return False
      if arr[i: i + 1, j + 6: j + 7] != 1:
        return False
      if arr[i + 1: i + 2, j + 7: j + 8] != 1:
        return False
      if arr[i + 1: i + 2, j + 10: j + 11] != 1:
        return False
      if arr[i: i + 1, j + 11: j + 12] != 1:
        return False
      if arr[i: i + 1, j + 12: j + 13] != 1:
        return False
      if arr[i + 1: i + 2, j + 13: j + 14] != 1:
        return False
      if arr[i + 1: i + 2, j + 16: j + 17] != 1:
        return False
      if arr[i: i + 1, j + 17: j + 18] != 1:
        return False
      if arr[i: i + 1, j + 18: j + 19] != 1:
        return False
      if arr[i: i + 1, j + 19: j + 20] != 1:
        return False
      if arr[i - 1: i, j + 18: j + 19] != 1:
        return False
      return True
    except IndexError as e:
      print(str(e))
      return False
  
  def change_to_twos(i, j, arr):
    arr[i:i + 1, j:j + 1] = 2
    arr[i + 1: i + 2, j + 1: j + 2] = 2
    arr[i + 1: i + 2, j + 4: j + 5] = 2
    arr[i: i + 1, j + 5: j + 6] = 2
    arr[i: i + 1, j + 6: j + 7] = 2
    arr[i + 1: i + 2, j + 7: j + 8] = 2
    arr[i + 1: i + 2, j + 10: j + 11] = 2
    arr[i: i + 1, j + 11: j + 12] = 2
    arr[i: i + 1, j + 12: j + 13] = 2
    arr[i + 1: i + 2, j + 13: j + 14] = 2
    arr[i + 1: i + 2, j + 16: j + 17] = 2
    arr[i: i + 1, j + 17: j + 18] = 2
    arr[i: i + 1, j + 18: j + 19] = 2
    arr[i: i + 1, j + 19: j + 20] = 2
    arr[i - 1: i, j + 18: j + 19] = 2
  
  cp = copy.deepcopy(image)
  num_rotated = 0
  while (np.array_equal(cp, image)):
    for i in range(1, total - sides*2 - 1):
      for j in range(total - sides*2 - 19):
        if image[i: i+1, j:j+1] != 1:
          continue
        if pattern_check(i, j, image) == True:
          change_to_twos(i, j, cp)
    if np.array_equal(cp, image) == False:
      break
    cp = np.rot90(cp)
    image = np.rot90(image)
    num_rotated += 1
    if num_rotated == 4:
      cp = np.fliplr(cp)
      image = np.fliplr(image)
    if num_rotated == 8:
      cp = np.fliplr(cp)
      image = np.fliplr(image)
      cp = np.flipud(cp)
      image = np.flipud(image)
    if num_rotated == 12:
      cp = np.flipud(cp)
      image = np.flipud(image)
      cp = np.fliplr(cp)
      image = np.fliplr(image)
      cp = np.flipud(cp)
      image = np.flipud(image)
    if num_rotated == 16:
      cp = np.flipud(cp)
      image = np.flipud(image)
      cp = np.fliplr(cp)
      image = np.fliplr(image)
      cp = np.flipud(cp)
      image = np.flipud(image)
      cp = np.fliplr(cp)
      image = np.fliplr(image)
    if num_rotated == 20:
      break
  
  
  
  print(cp)
  count = 0
  for i in range(total - sides*2):
    for j in range(total - sides*2):
      if cp[i: i+1, j:j+1] == 1:
        count += 1

      



  return num, count




  





          


      


  

