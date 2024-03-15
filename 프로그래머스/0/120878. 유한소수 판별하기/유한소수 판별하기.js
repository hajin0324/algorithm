function solution(a, b) {
    let gcd = 0;
    
    for (let i = a; i >= 1; i--) {
        if (a % i == 0 && b % i == 0) {
            gcd = i;
            break;
        }
    }
    
    b /= gcd;
    while (b % 2 == 0) b /= 2;
    while (b % 5 == 0) b /= 5;
    
    return b == 1 ? 1 : 2;
}