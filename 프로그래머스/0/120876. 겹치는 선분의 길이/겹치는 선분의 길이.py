def solution(lines):
    cnt = [0] * 200
    
    for line in lines:
        for i in range(line[0], line[1]):
            cnt[i + 100] += 1 
            
    return len([i for i in cnt if i > 1])