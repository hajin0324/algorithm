def in_range(x, y, w, h):
    return -w <= x and x <= w and -h <= y and y <= h

def solution(keyinput, board):
    x, y = 0, 0
    dir = {'up' : 0, 'down' : 1, 'left' : 2, 'right' : 3}
    dxs, dys = [0, 0, -1, 1],[1, -1, 0, 0]
           
    for i in keyinput:
        d_num = dir[i]
        dx, dy = x + dxs[d_num], y + dys[d_num]
        
        if in_range(dx, dy, board[0] // 2, board[1] // 2):
           x, y = dx, dy
           
    return [x, y]