x = int(input())
y = int(input())
result = 0

if x > 0:
  result = 1 if y > 0 else 4
else:
  result = 2 if y > 0 else 3

print(result)