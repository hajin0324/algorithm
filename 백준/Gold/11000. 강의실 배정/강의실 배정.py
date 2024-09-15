from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
time = []
ans = 1

for _ in range(n):
  t = list(map(int, input().split()))
  time.append(t)

time.sort()

que = PriorityQueue()
que.put(time[0][1])

for i in range(1, len(time)):
  small = que.get()
  if time[i][0] < small:
    que.put(small)
    ans += 1
  
  que.put(time[i][1])

print(ans)