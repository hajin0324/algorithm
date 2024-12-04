from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque()
    cities = [c.lower() for c in cities]
    
    for c in cities:  
        if cacheSize == 0:
                time += 5
                continue
                
        if c in cache:
            cache.remove(c)
            time += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            time += 5
        cache.append(c)
                
    return time