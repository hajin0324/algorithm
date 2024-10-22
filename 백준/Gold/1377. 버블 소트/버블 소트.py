import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
  nums.append((int(input()), i))

sorted_nums = sorted(nums)

ans = 0
for i in range(n):
  if ans < sorted_nums[i][1] - i:
    ans = sorted_nums[i][1] - i

print(ans + 1)