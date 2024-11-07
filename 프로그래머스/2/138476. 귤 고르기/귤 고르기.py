def solution(k, tangerine):
    tan = dict()
    
    for t in tangerine:
        if t in tan:
            tan[t] += 1
        else:
            tan[t] = 1
    
    sorted_tan = sorted(tan.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    
    for t, n in sorted_tan:
        k -= n
        ans += 1
        
        if k <= 0:
            return ans