def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n


def solution(board):
    bomb = [[0 for _ in range(len(board))] 
            for _ in range(len(board))]
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                bomb[i][j] = 1
                
                for dx, dy in zip(dxs, dys):
                    dx, dy = i + dx, j + dy
                    
                    if in_range(dx, dy, len(board)):
                        bomb[dx][dy] = 1
                        
    cnt = 0
    for rows in bomb:
        for elem in rows:
            if elem == 0:
                cnt += 1
                
    return cnt