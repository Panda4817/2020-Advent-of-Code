import nltk
nltk.download('punkt')

import collections

def part1(data):
  lst = data.split("\n\n")
  rules = {}
  for r in lst[0].split("\n"):
    parts = r.split(": ")
    sub = parts[1].split(" | ")
    arr = []
    for s in sub:
      try:
        arr.append([int(i) for i in s.split()])
      except:
        arr.append([i for i in s.split('"') if i != '' ])
      
    rules[int(parts[0])] = arr

  od = collections.OrderedDict(sorted(rules.items()))
  

  TERMINALS = """"""
  NONTERMINALS = """"""
  for k,v in od.items():
    if len(v[0]) == 1 and str(v[0][0]).isalpha():
      TERMINALS += str(k) + ' -> "' + v[0][0] + '"\n'
    else:
      if k == 8:
        NONTERMINALS += '8 -> 42 | 42 8\n'
      elif k == 11:
        NONTERMINALS += '11 -> 42 31 | 42 11 31\n'
      else:
        NONTERMINALS += str(k) + ' -> '
        for s in v:
          NONTERMINALS += " ".join([str(i) for i in s])
          if v.index(s) != len(v) - 1:
            NONTERMINALS += " | "
          else:
            NONTERMINALS += "\n"
  
  print(TERMINALS)
  print(NONTERMINALS)
  
  grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
  parser = nltk.ChartParser(grammar)

  m = lst[1].split("\n")
  count = 0
  for p in m:
    if list(parser.parse(list(p))):
      print(p)
      count += 1

  return count

# Part 2 in part 1