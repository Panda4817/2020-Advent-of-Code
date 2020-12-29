import collections
# part 2 in part 1
def part1(data):
  lst = data.split("\n")
  allergens = []
  alls = []
  inglst = []
  for l in lst:
    parts = l.split("(contains ")
    al = parts[1].split(", ")
    al[-1] = al[-1].split(")")[0]
    ing = parts[0].split()
    for i in ing:
      if i not in inglst:
        inglst.append(i)
    allergens.append({'contains': al, 'ing': ing })
    for a in al:
      if a not in alls:
        alls.append(a)
  
  filtered = {}
  nt = []
  for a in alls:
    filtered[a] = []
    options = {}
    for i in inglst:
      options[i] = 0
    number = 0
    for b in allergens:
      if a not in b['contains']:
        continue
      number += 1
      for val in b['ing']:
        options[val] += 1
    print(a, number)
    for k, v in options.items():
      if v >= number:
        filtered[a].append(k)
  
  for f, v in filtered.items():
    if len(v) == 1:
      for ke, ve in filtered.items():
        if ke == f:
          continue
        if v[0] in ve:
          ve.remove(v[0])
  
  for f, v in filtered.items():
    if len(v) > 1:
      options = {}
      for val in v:
        options[val] = 0
      for val in v:
        for ke, ve in filtered.items():
          if ke == f:
            continue
          if val in ve:
            options[val] += 1
      
      keep = None
      for o in options.keys():
        if options[o] == 0:
          keep = o
      
      for o in options.keys():
        if options[o] > 0 and keep != None:
          if o in v:
            v.remove(o)
  
  for f, v in filtered.items():
    if len(v) == 1:
      for ke, ve in filtered.items():
        if ke == f:
          continue
        if v[0] in ve:
          ve.remove(v[0])
  
  for k, v in filtered.items():
    print(k, v)
  
  od = collections.OrderedDict(sorted(filtered.items()))
  
  a = [j for i in od.values() for j in i]
  print(",".join(a)) # Answer to part 2
  
  for k in inglst:
    if k not in a:
      nt.append(k)
  
  num = 0
  for a in allergens:
    for val in a['ing']:
      if val in nt:
        num += 1

  return num # part 1 answer
          
  
    