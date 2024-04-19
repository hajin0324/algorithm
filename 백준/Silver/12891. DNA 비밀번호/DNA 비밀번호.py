s, p = map(int, input().split())
dna = input()
num = list(map(int, input().split()))
cnt = {"A": 0, "C": 0, "G": 0, "T": 0}
result = 0

# DNA 문자열 확인
def check():
  return cnt["A"] >= num[0] and cnt["C"] >= num[1] and cnt["G"] >= num[2] and cnt["T"] >= num[3]

# 초기 부분 문자열 확인
for i in range(p):
  cnt[dna[i]] += 1

if check():
  result += 1

# 한 칸씩 이동하며 부분 문자열 확인  
start, end = 1, p
while end < s:
  cnt[dna[start - 1]] -= 1
  cnt[dna[end]] += 1

  if check():
    result += 1

  start += 1
  end += 1

print(result)