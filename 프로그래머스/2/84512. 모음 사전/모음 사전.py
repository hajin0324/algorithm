from collections import deque

def solution(word):
    ans = 0
    alp = ['A', 'E', 'I', 'O', 'U']
    
    for i, w in enumerate(word):
        weight = sum(5 ** j for j in range(4 - i, -1, -1))
        ans += weight * alp.index(w) + 1
    
    return ans