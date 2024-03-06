def solution(balls, share):
    return fact(balls) / (fact(balls - share) * fact(share))

def fact(n):
    return n * fact(n - 1) if n > 1 else 1