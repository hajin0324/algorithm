def solution(n):
    ans = []
    i = 2
    
    while n != 1:
        if n % i == 0:
            if i not in ans:
                ans.append(i)   
            n /= i
        else:
            i += 1
                
    return ans