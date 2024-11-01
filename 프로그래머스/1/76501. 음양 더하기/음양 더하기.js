function solution(absolutes, signs) {
    let nums = absolutes.map((e, i) => signs[i] ? e : -e)
    return nums.reduce((acc, cur) => acc + cur, 0)
}