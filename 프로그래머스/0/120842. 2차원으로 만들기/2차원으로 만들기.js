function solution(num_list, n) {
    let ans = [];
    
    for (let i = 0; i < num_list.length; i += n) {
        ans.push(num_list.slice(i, i + n));    
    }
    
    return ans;
}