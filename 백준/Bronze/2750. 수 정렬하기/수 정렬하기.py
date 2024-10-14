n = int(input())
nums = []

for _ in range(n):
  nums.append(int(input())) 


for i in range(n - 1):
  for j in range(n - i - 1):
    if nums[j] > nums[j + 1]:
      nums[j], nums[j + 1] = nums[j + 1], nums[j]

for n in nums:
  print(n)