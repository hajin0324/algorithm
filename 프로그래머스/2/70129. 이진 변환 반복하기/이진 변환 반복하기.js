function solution(s) {
    let ans = [0, 0];
    
    while (s != 1) {
        let len = s.length;
        ans[0] += 1;
        s = [...s].filter(e => e != 0);
        ans[1] += len - s.length;
        s = s.length.toString(2);
    }
    
    return ans;
}