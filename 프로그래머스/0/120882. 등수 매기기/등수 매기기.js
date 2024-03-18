function solution(score) {
    let avg = score.map(e => (e[0] + e[1]) / 2)
    let avg_sort = avg.slice().sort((a, b) => b - a)
    
    return avg.map(e => avg_sort.indexOf(e) + 1)
}