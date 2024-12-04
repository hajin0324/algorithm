def solution(clothes):
    closet = {}
    cnt = 1
    
    for c, t in clothes:
        if t in closet:
            closet[t] += 1
        else:
            closet[t] = 1
            
    for value in closet.values():
        cnt *= (value + 1)
            
    return cnt - 1