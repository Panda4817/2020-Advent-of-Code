def part1(data):
  public_keys = [int(i) for i in data.split("\n")]
  print(public_keys)
  loop_sizes = []
  for pk in public_keys:
    sn = 7
    v = 1
    l = 0
    while(v != pk):
      l += 1
      v = v * sn
      v = v % 20201227 
    loop_sizes.append(l)
  print(loop_sizes)

  sn = public_keys[0]
  v = 1
  for i in range(loop_sizes[1]):
    v = v * sn
    v = v % 20201227
  
  return v