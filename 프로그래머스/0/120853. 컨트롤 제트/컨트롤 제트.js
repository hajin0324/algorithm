function solution(s) {
    let prev = 0;
    
    return s.split(' ').reduce((acc, curr, idx) => {
        if (curr === 'Z') {
            return acc - prev;
        } else {
            prev = Number(curr);
            return acc + Number(curr);
        }
    }, 0);
}