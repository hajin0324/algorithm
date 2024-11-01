function solution(s) {
    let len = s.length;
    let mid = Math.floor(len / 2)
    return len % 2 == 0 ? s[mid - 1] + s[mid] : s[mid]
}