n = int(input())
nums = list(map(int, input().split()))
line = [nums[0]]

for i in range(n - 1):
  for j in range(i, -1, -1):
    if nums[i + 1] > line[j]:
      line.insert(j + 1, nums[i + 1])
      break
    
  if len(line) < i + 2:
    line.insert(0, nums[i + 1])

s = [line[0]]
for i in range(1, n):
  s.append(s[i - 1] + line[i])

print(sum(s))