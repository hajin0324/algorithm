function solution(chicken) {
    let service = 0
    
    while (chicken >= 10) {
        service += Math.floor(chicken / 10)
        chicken = chicken % 10 + Math.floor(chicken / 10)
    }
    
    return service
}