def part1(data):
  nums = [int(n) for n in data.split(",")]
  length = len(nums)
  turns = {}
  last_number = 0
  turn = 2020
  for i in range(length):
    turns[nums[i]] = []
    turns[nums[i]].append(i + 1)
    last_number = nums[i]
  print(turns)
  for i in range(length + 1, turn + 1):
    if len(turns[last_number]) == 1:
      turns[0].append(i)
      last_number = 0
    else:
      new_number = turns[last_number][-1] - turns[last_number][-2]
      if new_number in turns.keys():
        turns[new_number].append(i)
      else:
        turns[new_number] = []
        turns[new_number].append(i)
      last_number = new_number
    print(last_number)
  
  print(turns)
  return last_number