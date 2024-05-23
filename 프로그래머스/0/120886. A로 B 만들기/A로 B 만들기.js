function solution(before, after) {
    let bList = [...(before)].sort().join('');
    let aList = [...(after)].sort().join('');
    return bList == aList ? 1 : 0;
}