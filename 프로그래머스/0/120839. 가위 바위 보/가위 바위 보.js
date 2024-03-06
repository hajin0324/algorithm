function solution(rsp) {
    return rsp.split('').map(e => {
        if (e == 2) return 0;
        else if (e == 0) return 5;
        else return 2;
    }).join('');
}