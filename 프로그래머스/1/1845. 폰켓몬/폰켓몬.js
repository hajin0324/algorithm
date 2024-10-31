function solution(nums) {
    let limit = nums.length / 2
    let monster = [...new Set(nums)]
    
    return monster.length >= limit ? limit : monster.length
}