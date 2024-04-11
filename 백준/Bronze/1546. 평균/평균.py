n = int(input())
score = list(map(int, input().split()))

s_max = max(score)
s_sum = sum(score)

print(s_sum * 100 / s_max / n)