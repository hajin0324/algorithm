# 모듈 설정
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

arr = [[0] * (n + 1)]
for _ in range(n):
  row = [0] + [int(x) for x in input().split()]
  arr.append(row) 

# 합 배열 만들기
sums = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  for j in range(1, n + 1):
    sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1] + arr[i][j]

# 구간 합 구하기
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(sums[x2][y2] - sums[x1 - 1][y2] - sums[x2][y1 - 1] + sums[x1 - 1][y1 - 1])