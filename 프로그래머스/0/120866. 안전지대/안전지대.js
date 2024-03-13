function solution(board) {
    const inRange = function(x, y, n) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }
    
    const n = board.length;
    let bomb = board.map(v => [...v])
    const dxs = [-1, -1, -1, 0, 1, 1, 1, 0];
    const dys = [-1, 0, 1, 1, 1, 0, -1, -1];
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] == 1) {
    
                for (let k = 0; k < 8; k++) {
                    x = i + dxs[k], y = j + dys[k];
                    if (inRange(x, y, n)) {
                        bomb[x][y] = 1;
                    }
                }
            }    
        }
    }
        
    return bomb.flat().filter(e => !e).length;
}