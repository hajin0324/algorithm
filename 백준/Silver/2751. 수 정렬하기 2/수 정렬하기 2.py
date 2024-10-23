import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = []
for _ in range(n):
  nums.append(int(input()))

def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  
  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])

  return merge(left, right)

def merge(left, right):
  result = []
  lc = rc = 0

  while lc < len(left) and rc < len(right):
    if left[lc] < right[rc]:
      result.append(left[lc])
      lc += 1
    else:
      result.append(right[rc])
      rc += 1

  result += left[lc:]
  result += right[rc:]

  return result

nums = merge_sort(nums)

for num in nums:
  print(str(num) + '\n')