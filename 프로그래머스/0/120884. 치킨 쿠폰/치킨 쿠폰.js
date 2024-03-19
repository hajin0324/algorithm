function solution(chicken) {
    let coupon = chicken % 10 + parseInt(chicken / 10)
    let cnt = parseInt(chicken / 10)
    
    while (coupon >= 10) {
        cnt += parseInt(coupon / 10)
        coupon = parseInt(coupon / 10) + coupon % 10
    }
    
    return cnt
}