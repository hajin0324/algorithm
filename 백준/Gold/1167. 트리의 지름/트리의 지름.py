from collections import deque

v = int(input())
tree = [[] for _ in range(v + 1)]
for _ in range(v):
  inp = list(map(int, input().split()))
  for i in range(1, len(inp) - 2, 2):
    tree[inp[0]].append((inp[i], inp[i + 1]))

def bfs(i):
  q = deque()
  q.append((i, 0))
  far = [i, 0]

  while q:
    node, cnt = q.pop()

    if cnt > far[1]:
      far[0], far[1] = node, cnt

    visited[node] = True
    for n, d in tree[node]:
      if not visited[n]:
        q.append((n, cnt + d))

  return far

visited = [False] * (v + 1)
big = bfs(1)

visited = [False] * (v + 1)
long = bfs(big[0])
print(long[1])