n = int(input())
next = 1
stack = []
result = []
can = True

for _ in range(n):
  num = int(input())

  if not len(stack):
    stack.append(next)
    next += 1
    result.append("+")

  while True:
    if num == stack[-1]:
      stack.pop()
      result.append("-")
      break
    elif num < stack[-1]:
      if num < next:
        can = False
        break
      else:
        stack.pop()
        result.append("-")
    else:
      stack.append(next)
      next += 1
      result.append("+")



if not can:
  print("NO")
else:
  for i in result:
    print(i)