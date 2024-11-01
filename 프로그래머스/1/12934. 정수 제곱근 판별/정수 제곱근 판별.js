function solution(n) {
    s = Math.sqrt(n)
    return Number.isInteger(s) ? Math.pow(s + 1, 2) : -1
}