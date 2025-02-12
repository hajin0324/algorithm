import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
N = len(A)
M = [[0, 2, 2, 2, 2], 
     [2, 1, 3, 4, 3], 
     [2, 3, 1, 3, 4], 
     [2, 4, 3, 1, 3], 
     [2, 3, 4, 3, 1]]

D = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
D[0][0][0] = 0

for i in range(1, N):
  p = A[i - 1]

  for j in range(5):
    if j == p:
      continue
    for k in range(5):
      D[i][j][p] = min(D[i - 1][j][k] + M[k][p], D[i][j][p])

  for j in range(5):
    if j == p:
      continue
    for k in range(5):
      D[i][p][j] = min(D[i - 1][k][j] + M[k][p], D[i][p][j])

result = min(D[N - 1][i][j] for i in range(5) for j in range(5))
print(result)