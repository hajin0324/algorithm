function solution(n) {
    let ans = [];
    let i = 2;
    
    while (n != 1) {
        if (n % i == 0) {
            if (!ans.indexof(i)) {
                ans.push(i);
            }
            ans /= i;
        }  
        else {
            i++;
        }
    }
        
    return ans;
}