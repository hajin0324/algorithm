import sys
input = sys.stdin.readline

N = int(input())
M = [(0, 0)]
for _ in range(N):
  x, y = map(int, input().split())
  M.append((x, y))
D = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

def execute(s, e):
  val = sys.maxsize

  if D[s][e] != -1:
    return D[s][e]
  
  if s == e:
    return 0
  
  if s + 1 == e:
    return M[s][0] * M[e][0] * M[e][1]

  for i in range(s, e):
    val = min(val, M[s][0] * M[i][1] * M[e][1] + execute(s, i) + execute(i + 1, e))

  D[s][e] = val
  return D[s][e]

print(execute(1, N))