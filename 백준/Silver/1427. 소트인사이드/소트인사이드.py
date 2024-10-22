n = list(input())

for i in range(len(n)):
  big = i

  for j in range(i + 1, len(n)):
    if n[big] < n[j]:
      big = j

  if n[i] < n[big]:
    n[big], n[i] = n[i], n[big]

print(''.join(n))