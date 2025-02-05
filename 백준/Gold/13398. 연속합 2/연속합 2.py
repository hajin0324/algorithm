import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = A[0]

L = [0] * N
L[0] = A[0]

for i in range(1, N):
  L[i] = max(L[i - 1] + A[i], A[i])
  result = max(result, L[i])

R = [0] * N
R[N - 1] = A[N - 1]

for i in range(N - 2, -1, -1):
  R[i] = max(R[i + 1] + A[i], A[i])

for i in range(1, N - 1):
  result = max(result, L[i - 1] + R[i + 1])

print(result)