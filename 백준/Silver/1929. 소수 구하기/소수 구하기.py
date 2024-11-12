n, m = map(int, input().split())
isPrime = [True] * (m + 1)

isPrime[1] = False
for i in range(2, int(m ** 0.5) + 1):
  if isPrime[i]:
    for j in range(i + i, m + 1, i):
      isPrime[j] = False

for i in range(n, m + 1):
  if isPrime[i]:
    print(i)