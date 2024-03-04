function solution(n) {
    return Array(n).fill(1).map((v, i) => v + i).filter(e => n % e == 0).length;
}