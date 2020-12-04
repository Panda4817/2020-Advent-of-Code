import re

def part1(data):
  lst = data.split("\n\n")
  have = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  count = 0
  for p in lst:
    num = 0
    n = p.split(":") 
    for e in n:
      for h in have:
         if h in e: num += 1
    if num == 7: count += 1
  return count

def part2(data):
  lst = data.split("\n\n")
  eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  count = 0
  for p in lst:
    num = 0
    n = p.split(" ")
    updated_n = []
    for e in n:
      if "\n" in e:
        t = e.split("\n")
        for s in t:
          updated_n.append(s)
      else: updated_n.append(e)
    
    for el in updated_n:
      kv = el.split(":")
      if kv[0] == 'byr' and int(kv[1]) >= 1920 and int(kv[1]) <= 2002:
        num += 1
      elif kv[0] == 'iyr' and int(kv[1]) >= 2010 and int(kv[1]) <= 2020:
        num += 1
        
      elif kv[0] == 'eyr' and int(kv[1]) >= 2020 and int(kv[1]) <= 2030:
        num += 1
     
      elif kv[0] == 'hgt' and re.search('^[0-9]+(cm|in)$', kv[1]):
        if 'cm' in kv[1]:
          g = kv[1].split('cm')
          if int(g[0]) >= 150 and int(g[0]) <= 193:
            num += 1
           
        elif 'in' in kv[1]:
          g = kv[1].split('in')
          if int(g[0]) >= 59 and int(g[0]) <= 76:
            num += 1
            
      elif kv[0] == 'hcl' and re.search('^[#][0-9a-f]{6}$', kv[1]):
        num += 1
        
      elif kv[0] == 'ecl' and kv[1] in eye_colours:
        num += 1
        
      elif kv[0] == 'pid' and re.search('^[0-9]{9}$', kv[1]):
        num += 1
      
    if num == 7: 
      count += 1
  
  return count