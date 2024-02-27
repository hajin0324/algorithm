def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    den = denom1 * denom2
    gcd = 0
    
    for i in range(min(num, den), 0, -1):
        if num % i == 0 and den % i == 0:
            gcd = i
            break
    
    return [num / gcd, den / gcd]