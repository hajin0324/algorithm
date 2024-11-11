form = input().split("-")

ans = sum(map(int, form[0].split("+")))
form = form[1:]

while form:
  fo = form.pop()
  ans -= sum(map(int, fo.split("+")))

print(ans)