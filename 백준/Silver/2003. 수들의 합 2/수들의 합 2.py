n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

start = 0
end = 0
sum = li[0]

while start < len(li):
  if sum == m:
    cnt += 1
    sum -= li[start]
    start += 1
  elif sum < m and end < len(li) - 1:
    end += 1
    sum += li[end]
  else:
    sum -= li[start]
    start += 1

print(cnt)