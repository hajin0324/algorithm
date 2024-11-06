def gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i

def lcm(n, m):
    return n * m // gcd(n, m)
        
def solution(arr):
    n = arr[0]
    for i in arr[1:]:
        n = lcm(n, i)
        
    return n