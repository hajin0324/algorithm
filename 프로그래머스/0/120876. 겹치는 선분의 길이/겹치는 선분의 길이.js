function solution(lines) {
    const max = Math.max(...lines.flat());
    const min = Math.min(...lines.flat());
    let cnt = new Array(max - min).fill(0);
    
    lines.forEach(line => {
        for (let i = line[0]; i < line[1]; i++) {
            cnt[i - min]++;
        }    
    })
    
    return cnt.filter(e => e > 1).length;
}