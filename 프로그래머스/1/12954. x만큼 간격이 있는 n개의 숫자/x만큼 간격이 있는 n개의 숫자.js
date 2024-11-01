function solution(x, n) {
    return [...Array(n)].map((e, i) => x * (i + 1))
}