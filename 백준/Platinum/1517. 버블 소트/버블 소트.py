import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  
  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])

  return merge(left, right)

def merge(left, right):
  global cnt
  result = []
  lc = rc = 0

  while lc < len(left) and rc < len(right):
    if left[lc] <= right[rc]:
      result.append(left[lc])
      lc += 1
    else:
      result.append(right[rc])
      cnt += len(left) - lc
      rc += 1

  result += left[lc:]
  result += right[rc:]

  return result

nums = merge_sort(nums)
print(cnt)