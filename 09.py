def part1(data):
  nums = [int(n) for n in data.split("\n")]
  preamble = 25
  for n in range(preamble, len(nums)):
    add_up_to = nums[n]
    found = False
    for p1 in range(n-preamble, n):
      for p2 in range(p1 + 1, n):
        if nums[p1] + nums[p2] == add_up_to:
          found  = True
        if found:
          break
      if found:
        break
    if found == False:
      return add_up_to

def part2(data): 
  nums = [int(n) for n in data.split("\n")]
  num = part1(data)
  temp = num
  contigious = []
  i = 0
  while(temp != 0):
    if temp == 0:
      break
    temp = num
    contigious.clear()
    for n in range(i, len(nums)):
      if nums[n] != num:
        temp -= nums[n]
        contigious.append(nums[n])
      if temp == 0:
        break
    i += 1
  return max(contigious) + min(contigious)
