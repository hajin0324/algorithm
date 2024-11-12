n, m = map(int, input().split())
isPrime = [True] * (int(m ** 0.5) + 1)
isPrime[1] = False

for i in range(2, len(isPrime)):
  if isPrime[i]:
    for j in range(i + i, len(isPrime), i):
      isPrime[j] = False

almost = set()
for i in range(2, len(isPrime)):
  if isPrime[i]:
    num = i * i
    while num <= m:
      if n <= num:
        almost.add(num)
      
      num *= i

print(len(almost))