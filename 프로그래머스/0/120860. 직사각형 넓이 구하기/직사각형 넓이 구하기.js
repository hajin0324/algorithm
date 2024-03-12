function solution(dots) {
    let x = Math.max(...dots.map(d => d[0])) - Math.min(...dots.map(d => d[0]));
    let y = Math.max(...dots.map(d => d[1])) - Math.min(...dots.map(d => d[1]));
    
    return x * y;
}