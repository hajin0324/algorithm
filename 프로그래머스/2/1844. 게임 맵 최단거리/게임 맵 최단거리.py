from collections import deque

def in_range(x, y, n, m):
    return 0 <= x and x < n and 0 <= y and y < m

def solution(maps):
    n, m = len(maps), len(maps[0])
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    q = deque([(0, 0, 1)])
    
    while q:
        x, y, cnt = q.popleft()
    
        if x == n - 1 and y == m - 1:
            return cnt

        for dx, dy in zip(dxs, dys):
            rx = x + dx
            ry = y + dy

            if in_range(rx, ry, n, m) and maps[rx][ry] == 1:
                maps[rx][ry] += 1
                q.append((rx, ry, cnt + 1))
    return -1