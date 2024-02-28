function solution(array) {
    let cnt = new Array(1001).fill(0);
    
    for (let i of array) {
        cnt[i]++;
    }

    let n = 0;
    for (let c of cnt) {
        if (c == Math.max(...cnt)) {
            n++;
        }
    }

    if (n > 1) {
        return -1;
    } else {
        return cnt.indexOf(Math.max(...cnt));
    }
}