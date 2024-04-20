n = int(input())
next = 1
stack = []
result = []
can = True

for _ in range(n):
  num = int(input())

  if num >= next:
    while num >= next:
      stack.append(next)
      next += 1
      result.append("+")
    stack.pop()
    result += "-"

  else:
    if num < stack[-1]:
      can = False
      break
    else:
      stack.pop()
      result.append("-")

if not can:
  print("NO")
else:
  for i in result:
    print(i)