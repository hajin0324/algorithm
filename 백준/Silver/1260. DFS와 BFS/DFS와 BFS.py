from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n + 1):
  graph[i].sort()


def dfs(node):
  print(node, end=' ')
  visited[node] = True

  for i in graph[node]:
    if not visited[i]:
      dfs(i)


def bfs(v):
  queue = deque()
  queue.append(v)
  visited[v] = True

  while queue:
    q = queue.popleft()
    print(q, end=' ')

    for i in graph[q]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)


dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)