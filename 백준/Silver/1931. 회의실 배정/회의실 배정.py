n = int(input())
meeting = []
for i in range(n):
  s, e = map(int, input().split())
  meeting.append([s, e])

meeting.sort(key = lambda x: (x[1], x[0]))
fin = meeting[0][1]
ans = 1

for i in range(1, n):
  if meeting[i][0] >= fin:
    fin = meeting[i][1]
    ans += 1
    
print(ans)