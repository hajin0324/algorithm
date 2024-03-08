function solution(n) {
    let num = 3628800;
    
    for (let i = 10; i >= 1; i--) {
        if (num <= n) {
            return i
        }
        num /= i;
    }
}