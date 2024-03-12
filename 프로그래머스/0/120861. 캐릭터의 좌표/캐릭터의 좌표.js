function solution(keyinput, board) {
    const inRange = function (x, y, w, h) {
        return -w <= x && x <= w && -h <= y && y <= h;
    };
    
    let x = 0, y = 0;
    let dir = {'up' : 0, 'down' : 1, 'left' : 2, 'right' : 3};
    let dxs = [0, 0, -1, 1], dys = [1, -1, 0, 0];
    
    keyinput.forEach(key => {
        d_num = dir[key];
        dx = x + dxs[d_num];
        dy = y + dys[d_num];
        
        if (inRange(dx, dy, Math.floor(board[0] / 2), Math.floor(board[1] / 2))) {
            x = dx;
            y = dy;
        }
    });
    
    return [x, y];
}