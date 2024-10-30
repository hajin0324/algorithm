n, m = map(int, input().split())
course = list(map(int, input().split()))
s, e = max(course), sum(course)

while s <= e:
  mid = (s + e) // 2
  blueray = 1
  cnt = 0

  for i in course:
    if cnt + i <= mid:
      cnt += i
    else:
      blueray += 1
      cnt = i

  if blueray <= m:
    e = mid - 1
  else:
    s = mid + 1

print(s)