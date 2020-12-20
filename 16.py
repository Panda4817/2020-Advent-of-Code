def part1(data):
  lst = data.split("\n\n")
  rules = []
  wrong = []
  valid = []
  current_order = []
  for i in lst[0].split("\n"):
    nums = i.split(": ")
    current_order.append(nums[0])
    parts = nums[1].split(" or ")
    arr = []
    for p in parts:
      sub = p.split("-")
      t = (int(sub[0]), int(sub[1]))
      arr.append(t)
    rules.append(arr)
  for i in lst[2].split("\n"):
    if i == 'nearby tickets:':
      continue
    nums = [int(n) for n in i.split(",")]
    valid_check = 0
    for n in nums:
      invalid = 0
      for r in rules:
        for q in r:
          if n < q[0] or n > q[1]:
            invalid += 1
      if invalid == len(rules) * 2:
        wrong.append(n)
        valid_check += 1
    if valid_check == 0:
      valid.append(nums)

  my_ticket = []
  for x in lst[1].split("\n"):
    if x != "your ticket:":
      for i in x.split(","):
        my_ticket.append(int(i))
  #return sum(wrong)
  print(sum(wrong))
  return [current_order, rules, my_ticket, valid]

def part2(data):
  info = part1(data)
  order = []
  length = len(info[0])
  for x in range(length):
    counts = []
    for r in range(length):
      count = 0
      for t in info[3]:
        if (t[x] >= info[1][r][0][0] and t[x] <= info[1][r][0][1]):
          count += 1
        elif (t[x] >= info[1][r][1][0] and t[x] <= info[1][r][1][1]):
          count += 1
      counts.append(count)
    arr = []  
    for c in range(len(counts)):
      if counts[c] == len(info[3]):
        arr.append(info[0][c])
    if len(arr) > 0:
      order.append(arr)
  
  new_order = {}
  while (len(new_order.keys()) < length):
    for o in range(len(order)):
      if len(order[o]) == 1:
        new_order[o] = order[o][0]
        for i in order:
          if order[o][0] in i and i != order[o]:
            i.remove(order[o][0])

  final = 1
  for k, v in new_order.items():
    if "departure " in v:
      final *= info[2][k]
  
  return final
          