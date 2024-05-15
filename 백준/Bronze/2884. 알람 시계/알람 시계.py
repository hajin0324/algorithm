h, m = map(int, input().split())

if m >= 45:
  h, m = h, m - 45
else:
  if h == 0:
    h, m = 23, m + 60 - 45
  else:
    h, m  = h - 1, m + 60 - 45

print(h, m)