N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

def binary(x):
  s, e = 0, N - 1
  while s <= e:
    mid = (s + e) // 2
    if A[mid] == x:
      return 1
    elif A[mid] > x:
      e = mid - 1
    else:
      s = mid + 1
  return 0

for b in B:
  ans = binary(b)
  print(1 if ans else 0)
