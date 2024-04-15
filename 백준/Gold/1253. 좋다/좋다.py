import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
good = 0

for i in range(n):
  s = 0
  e = n - 1
  
  while s < e:
    if arr[s] + arr[e] == arr[i]:
      if s != i and e != i:
        good += 1
        break
      elif s == i:
        s += 1
      else:
        e -=1
    elif arr[s] + arr[e] < arr[i]:
      s += 1
    else:
      e -= 1

print(good)