import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
relation = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
  a, b = map(int, input().split())
  relation[a].append(b)
  relation[b].append(a)


def abcde(peo, cnt):
  if cnt >= 5:
    print(1)
    exit()
  
  visited[peo] = True
  for i in relation[peo]:
    if not visited[i]:
      abcde(i, cnt + 1)
  visited[peo] = False


for i in range(n):
  abcde(i, 1)
  
print(0)