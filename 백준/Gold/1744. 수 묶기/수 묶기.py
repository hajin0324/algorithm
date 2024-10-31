from queue import PriorityQueue

n = int(input())
plus = PriorityQueue()
minus = PriorityQueue()
zero = False
ans = 0

for _ in range(n):
  inp = int(input())
  if inp > 1:
    plus.put(inp)
  elif inp < 0:
    minus.put(inp)
  elif inp == 0:
    zero = True
  else:
    ans += inp

if plus.qsize() % 2 != 0:
  plus.put(1)

def calc(nums):
  global ans 

  while nums.qsize() > 1:
    a = nums.get()
    b = nums.get()
    ans += (a * b)

calc(plus)
calc(minus)

if minus.qsize() == 1 and not zero:
  ans += minus.get()

print(ans)