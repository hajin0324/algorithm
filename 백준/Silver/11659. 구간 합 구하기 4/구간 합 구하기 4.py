import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0]
temp = 0
for num in nums:
  temp += num
  sums.append(temp)

for _ in range(m):
  i, j = map(int, input().split())
  print(sums[j] - sums[i - 1])