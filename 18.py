import operator

def part1(data):
  nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  operators = ['+', '*']

  problems = [p for p in data.split("\n")]
  answers = []
  
  for p in problems:
    temp = []
    current = []
    done = ''
    c = -1
    while(len(done) != len(p)):
      c += 1
      done += p[c]
      if p[c] == ' ' or p[c-1] == '(' or p[c-2] == '(':
        continue
      if p[c] in nums and c == 0:
        temp.append(int(p[c]))
      elif p[c] in operators:
        current.append(p[c])
      elif p[c] in nums and len(current) > 0:
        if len(current) > 1:
          if current[-1] == '+':
            temp[-1] += int(p[c])
          elif current[-1] == '*':
            temp[-1] *= int(p[c])
          del current[-1]
        else:
          if current[0] == '+':
            temp[-1] += int(p[c])
          elif current[0] == '*':
            temp[-1] *= int(p[c])
          del current[0]
      elif '(' in p[c]:
        x = c + 1
        char  = p[x]
        while(char == '('):
          temp.append(None)
          x +=1 
          char = p[x]
        temp.append(int(char))
      elif ')' in p[c] and len(current) > 0:
        length = len(temp)
        while(len(temp) != length - 1):
          if temp[-2] == None:
            temp[-2] = temp[-1]
            del temp[-1]
          elif len(current) > 1:
            if current[-1] == '+':
              temp[-2] += temp[-1]
            elif current[-1] == '*':
              temp[-2] *= temp[-1]
            del current[-1]
            del temp[-1]
          else:
            if current[0] == '+':
              temp[-2] += temp[-1]
            elif current[0] == '*':
              temp[-2] *= temp[-1]
            del current[0]
            del temp[-1]
      if problems.index(p) == 362:
        print(temp, current)
    print(p)
    if temp[0] != None:
      answers.append(temp[0])
    else:
      answers.append(temp[1])
  
  return sum(answers)

def part2(data):
  """
  Lowest precedence first: for part 2 "+" has higher precedence than "*"
  EXPRESSION -> TERM_A("*"TERM_A)*
  TERM_A -> TERM_B("+"TERM_B)*
  TERM_B -> "("EXPRESSION")"|NUMBER
  """
  def tokenize(data):
    operator_tokens = (
        '(', ')', '+', '*',
    )
    tokens = []
    t = ''

    for char in data:
      if char in operator_tokens:
        if t:
          tokens.append(t)
          t = ''
        tokens.append(char)
      elif char in (' ', '\n'):
        continue
      else:
        t += char
    if t:
      tokens.append(t)

    return tokens
  
  def parse(tokens):
    def _read_expression(index, func, char, op_func):
      """
      EXPRESSION -> FUNC(CHAR FUNC)*
      """
      val, index = func(index)
      while index < max_len:
        token = tokens[index]
        if token == char:
          index += 1  # Skip past operator
          val2, index = func(index)
          val = op_func(val, val2)
        else:
          break

      return val, index

    def read_expression(index):
      return _read_expression(index, read_term_a, '*', operator.mul)

    def read_term_a(index):
      return _read_expression(index, read_term_b, '+', operator.add)

    def read_term_b(index):
      token = tokens[index]
      if token == '(':
        index += 1  # Skip past opening bracket
        val, index = read_expression(index)
        index += 1  # Skip past closing bracket
      else:
        val, index = read_number(index)
      return val, index

    def read_number(index):
      token = tokens[index]
      return int(token), index + 1

    max_len = len(tokens)
    ans, _ = read_expression(0)

    return ans
  
  num = 0
  for d in data.split("\n"):
    tokens = tokenize(d)
    num += parse(tokens)
  
  return num

  
        
          
    


      

    



        
      
        
