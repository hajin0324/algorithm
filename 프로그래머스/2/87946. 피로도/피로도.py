ans = 0
visited = []

def solution(k, dungeons):
    global ans, visited
    visited = [0] * len(dungeons)
    explore(k, 0, dungeons)
    return ans


def explore(fa, cnt, dungeons):
    global ans
    
    if cnt > ans:
        ans = cnt
        
    for i in range(len(dungeons)):
        if fa >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            explore(fa - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0