def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = 0
    
    for i in range(min(numer, denom), 0, -1):
        if numer % i == 0 and denom % i == 0:
            gcd = i
            break
    
    return [numer / gcd, denom / gcd]