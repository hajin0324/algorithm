function solution(a, b) {
    ab = a.map((e, i) => e * b[i])
    return ab.reduce((acc, cur) => acc + cur, 0)
}