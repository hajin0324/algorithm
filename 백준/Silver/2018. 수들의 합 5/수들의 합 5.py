n = int(input())
cnt = 1
start = 1
end = 1
sumVal = 1

while end != n:
  if sumVal == n: 
    cnt += 1
    end += 1
    sumVal += end
  elif sumVal > n:
    sumVal -= start
    start += 1
  else:
    end += 1
    sumVal += end

print(cnt)