from collections import deque

def solution(priorities, location):
    cnt = 0
    queue =  deque([(idx, p) for idx, p in enumerate(priorities)])
    
    while True:
        p = queue.popleft()
        
        if any(p[1] < q[1] for q in queue):
            queue.append(p)
        else:
            cnt += 1
            if p[0] == location:
                break
            
    return cnt