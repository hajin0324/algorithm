str = input()
ans = ''

for s in str:
    if ord(s) < 97:
        ans += s.lower()
    else:
        ans += s.upper()
        
print(ans)