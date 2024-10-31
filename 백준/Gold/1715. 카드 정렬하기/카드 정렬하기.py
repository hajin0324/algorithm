from queue import PriorityQueue

n = int(input())
cards = PriorityQueue()
ans = 0

for _ in range(n):
  inp = int(input())
  cards.put(inp)

while cards.qsize() >= 2:
  a = cards.get()
  b = cards.get()

  ans += (a + b)
  cards.put(a + b)

print(ans)