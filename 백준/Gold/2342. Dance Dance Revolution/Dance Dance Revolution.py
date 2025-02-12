import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
A.pop()

C = [[0, 2, 2, 2, 2], 
     [2, 1, 3, 4, 3], 
     [2, 3, 1, 3, 4], 
     [2, 4, 3, 1, 3], 
     [2, 3, 4, 3, 1]]

D = [[sys.maxsize] * 5 for _ in range(5)]
D[0][0] = 0

for a in A:
  N = [[sys.maxsize] * 5 for _ in range(5)]

  for i in range(5):
    for j in range(5):
      if D[i][j] == sys.maxsize:
        continue

      if i == a or j == a:
        N[i][j] = min(N[i][j], D[i][j] + 1)

      else: 
        N[a][j] = min(N[a][j], D[i][j] + C[i][a])
        N[i][a] = min(N[i][a], D[i][j] + C[j][a])

  D = N

print(min(min(row) for row in D))