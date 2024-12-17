from collections import deque

def solution(word):
    ans = 0
    alp = ['A', 'E', 'I', 'O', 'U']
    q = deque([['A']])
    
    while q:
        w = q.popleft()
        ans += 1
        if ''.join(w) == word:
            break
            
        if len(w) != 5:
            w.append('A')
        else:
            if w[-1] == 'U':
                while w[-1] == 'U':
                    w.pop()

            idx = alp.index(w[-1]) 
            w[-1] = alp[idx + 1]
            
        q.append(w)
        
    return ans