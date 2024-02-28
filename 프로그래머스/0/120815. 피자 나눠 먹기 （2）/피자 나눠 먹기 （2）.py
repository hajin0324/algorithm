def solution(n):
    p = 1
    while True:
        if (p * 6) % n == 0:
            break
        p += 1
        
    return p