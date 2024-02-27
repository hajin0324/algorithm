function solution(numer1, denom1, numer2, denom2) {
    let num = numer1 * denom2 + numer2 * denom1;
    let den = denom1 * denom2;
    let gcd = 0;
    
    for (let i = Math.min(num, den); i >= 1; i--) {
        if (num % i == 0 && den % i == 0) {
            gcd = i;
            break;
        }
    }
    
    return [num / gcd, den / gcd]
}