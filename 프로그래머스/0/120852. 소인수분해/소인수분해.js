function solution(n) {
    let ans = [];
    let i = 2;
    
    while (n != 1) {
        if (n % i == 0) {
            ans.push(i)
            
            while (n % i == 0) {
                n /= i;
            }
        }
        i++;
    }
    return ans;
}