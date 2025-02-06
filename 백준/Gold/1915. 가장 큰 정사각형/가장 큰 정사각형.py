import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = [[0 for j in range(1001)] for i in range(1001)]
cnt = 0

for i in range(0, N):
  li = list(input())
  for j in range(0, M):
    D[i][j] = int(li[j])
    if D[i][j] == 1 and i > 0 and j > 0:
      D[i][j] = min(D[i - 1][j - 1], D[i - 1][j], D[i][j - 1]) + D[i][j]
    cnt = max(cnt, D[i][j])  

print(cnt * cnt)