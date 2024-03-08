from math import factorial

def solution(n):
    ans = 10
    
    while factorial(ans) > n:
        ans -= 1
        
    return ans