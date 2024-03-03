function solution(age) {
    let answer = '';
    
    for (let i of String(age).split('')) {
        answer += String.fromCharCode(97 + Number(i));
    }
    
    return answer;
}