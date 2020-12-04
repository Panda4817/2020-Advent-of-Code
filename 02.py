def part1(data):
  lst = list(data.split("\n"))
  overall = 0
  for e in lst:
    parts = e.split(" ")
    low_high = parts[0].split("-")
    letter = parts[1].split(":")[0]
    count = 0
    for l in parts[2]:
      if l == letter:
        count += 1
    if count >= int(low_high[0]) and count <= int(low_high[1]):
      overall += 1
  return overall

def part2(data):
  lst = list(data.split("\n"))
  overall = 0
  for e in lst:
    parts = e.split(" ")
    pos1_pos2 = parts[0].split("-")
    pos = [int(p) - 1 for p in pos1_pos2]
    letter = parts[1].split(":")[0]
    try:
      if parts[2][pos[0]] == letter and parts[2][pos[1]] != letter:
        overall += 1
      elif parts[2][pos[1]] == letter and parts[2][pos[0]] != letter:
        overall += 1
      else:
        continue
    except IndexError:
      continue
  return overall