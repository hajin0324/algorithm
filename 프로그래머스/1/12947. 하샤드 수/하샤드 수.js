function solution(x) {
    let sum = [...String(x)].map(Number).reduce((acc, cur) => acc + cur, 0)
    return x % sum == 0 ? true : false
}