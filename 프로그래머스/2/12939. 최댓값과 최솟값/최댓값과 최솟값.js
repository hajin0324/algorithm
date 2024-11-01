function solution(s) {
    let nums = s.split(" ");
    return Math.min(...nums) + " " + Math.max(...nums);
}