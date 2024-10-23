n, k = map(int, input().split())
nums = list(map(int, input().split()))

def quickSort(s, e, k):
  if s < e:
    p = findPivot(s, e)
    if p == k:
      return
    elif p < k:
      quickSort(p + 1, e, k)
    else:
      quickSort(s, p - 1, k)


def findPivot(s, e):
  if s + 1 == e:
    if nums[s] > nums[e]:
      nums[s], nums[e] = nums[e], nums[s]
    return e

  p = (s + e) // 2
  nums[s], nums[p] = nums[p], nums[s]
  pivot = nums[s]

  i, j = s + 1, e
  while i <= j:
    while nums[i] < pivot and i < (n - 1):
      i += 1
    while nums[j] > pivot and j > 0:
      j -= 1

    if i <= j:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
      j -= 1

  nums[s], nums[j] = nums[j], pivot
  return j

quickSort(0, n - 1, k - 1)
print(nums[k - 1])