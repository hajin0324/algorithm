function solution(balls, share) {
    const fact = (n) => {
        if (n < 1) {
            return 1
        } 
        return n * fact(n - 1)
    }
    
    return Math.round(fact(balls) / (fact(balls - share) * fact(share)));
}