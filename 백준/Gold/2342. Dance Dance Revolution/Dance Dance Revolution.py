import sys
input = sys.stdin.readline

def move_cost(s, e):
  if s == e:
    return 1
  elif s == 0:
    return 2
  elif (s - e + 4) % 2 != 0:
    return 3
  else:
    return 4

A = list(map(int, input().split()))
N = len(A)
D = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
D[0][0][0] = 0

for i in range(1, N):
  p = A[i - 1]

  for j in range(5):
    if j == p:
      continue
    for k in range(5):
      D[i][j][p] = min(D[i - 1][j][k] + move_cost(k, p), D[i][j][p])

  for j in range(5):
    if j == p:
      continue
    for k in range(5):
      D[i][p][j] = min(D[i - 1][k][j] + move_cost(k, p), D[i][p][j])

result = sys.maxsize
for i in range(5):
  for j in range(5):
    result = min(result, D[N - 1][i][j])

print(result)