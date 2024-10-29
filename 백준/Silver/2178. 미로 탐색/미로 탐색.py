from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
step = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < m

def bfs(i, j):
  q = deque()
  q.append((i, j))
  visited[i][j] = True
  step[i][j] = 1

  while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if in_range(nx, ny) and maze[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = True
        step[nx][ny] = step[x][y] + 1
        q.append((nx, ny))

bfs(0, 0)
print(step[n - 1][m - 1])