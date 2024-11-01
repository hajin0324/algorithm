function solution(n) {
    let cnt = 1;
    
    for (let i = 1; i <= Math.floor(n / 2); i++) {
        let sum = 0;
        let start = i;
        
        while (sum < n) {
            sum += start;
            start++;
        }
        
        if (sum == n) {
            cnt++;
        }
    }
    
    return cnt;
}