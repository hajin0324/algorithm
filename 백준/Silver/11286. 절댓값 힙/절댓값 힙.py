from queue import PriorityQueue
import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
q = PriorityQueue()

for _ in range(n):
  x = int(input())
  
  if x == 0:
    if q.empty():
      print("0\n")
    else:
      min_val = q.get()
      print(str(min_val[1]) + "\n")
  else:
    q.put((abs(x), x))