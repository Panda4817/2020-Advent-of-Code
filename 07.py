def part1(data):
  lst = data.split("\n")
  rules = {}
  gold = 'shiny gold'
  count = []
  to_check = [gold]
  for r in lst:
    parts = r.split(" bags contain ")
    rules[parts[0]] = []
    contains = parts[1].split(", ")
    for c in contains:
      sub_parts = c.split()
      if sub_parts[0] != 'no':
        rules[parts[0]].append(sub_parts[1] + ' ' + sub_parts[2])
  
  while(len(to_check) > 0):
    temp = []
    for k, v in rules.items():
      for b in v:
        if b in to_check:
          if k not in count:
            temp.append(k)
            count.append(k)
          break
    to_check = temp
  return len(count)

def part2(data):
  lst = data.split("\n")
  rules = {}
  gold = 'shiny gold'
  for r in lst:
    parts = r.split(" bags contain ")
    rules[parts[0]] = {}
    contains = parts[1].split(", ")
    for c in contains:
      sub_parts = c.split()
      if sub_parts[0] != 'no':
        rules[parts[0]][sub_parts[1] + ' ' + sub_parts[2]] = int(sub_parts[0])

  def recursion(colour):
    bag_total = 0
    for k, v in rules[colour].items():
      bag_total += v
      bag_total += recursion(k) * v
    return bag_total

  total = recursion(gold)

  return total