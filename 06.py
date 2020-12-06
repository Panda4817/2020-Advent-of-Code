def part1(data):
  lst = data.split("\n\n")
  count = 0
  az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  for l in lst:
    person = l.split("\n")
    found = []
    for p in person:
      for letter in az:
        if letter in p and letter not in found:
          found.append(letter)
    count += len(found)
  
  return count


def part2(data):
  lst = data.split("\n\n")
  count = 0
  az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  for l in lst:
    person = l.split("\n")
    for letter in az:
      found = 0
      for p in person:
        if letter in p: found += 1
      if found == len(person): count += 1
  
  return count