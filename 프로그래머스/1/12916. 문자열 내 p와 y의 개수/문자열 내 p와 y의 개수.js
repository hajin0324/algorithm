function solution(s){
    s = s.toLowerCase()
    let p = [...s].filter(e => e == 'p').length;
    let y = [...s].filter(e => e == 'y').length;

    return p == y ? true : false;
}