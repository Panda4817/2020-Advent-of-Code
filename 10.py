def part1(data):
  nums = [int(d) for d in data.split("\n")]
  sorted_nums = sorted(nums)
  built_in_adapter = sorted_nums[-1] + 3
  sorted_nums.append(built_in_adapter)
  sorted_nums.insert(0, 0)
  ones = 0
  threes = 0
  for i in range(len(sorted_nums) - 1):
    for j in range(i + 1, i + 2):
      if sorted_nums[j] - sorted_nums[i] == 1:
        ones += 1
      elif sorted_nums[j] - sorted_nums[i] == 3:
        threes += 1
  return ones * threes

def part2(data):
  nums = [int(d) for d in data.split("\n")]
  n = sorted(nums)
  built_in_adapter = n[-1] + 3
  n.append(built_in_adapter)
  n.insert(0, 0)
  must = []
  for i in range(len(n) - 1):
    for j in range(i + 1, i + 2):
      if n[j] - n[i] == 3:
        if n[i] not in must:
          must.append(n[i])
        if n[j] not in must:
          must.append(n[j])
  must.insert(0, 0)
  
  def num_of_arrangements(l):
    if l == 1:
      return 2
    elif l == 2:
      return 4
    elif l == 3:
      return 7

  a = 1
  for i in range(0, len(must) -1):
    xmin = n.index(must[i])
    xmax = n.index(must[i + 1])
    arr = n[xmin:xmax + 1]
    if len(arr) < 3:
      continue
    a *= num_of_arrangements(len(arr) - 2)
  
  return a
    