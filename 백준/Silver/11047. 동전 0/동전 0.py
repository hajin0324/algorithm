n, k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
  c = int(input())
  coins.append(c)

for coin in coins[-1::-1]:
  if coin <= k:
    cnt += k // coin
    k = k % coin

print(cnt)