function solution(s) {
    let arr = s.split(" ");
    return arr.map((e) => e.charAt(0).toUpperCase() + e.slice(1).toLowerCase()).join(" ");
}