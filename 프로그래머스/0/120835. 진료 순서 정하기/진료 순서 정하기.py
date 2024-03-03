def solution(emergency):
    arr = sorted(emergency, reverse=True)
    ans = []
    
    for e in emergency:
        ans.append(arr.index(e) + 1)
        
    return ans