function solution(id_pw, db) {
    let dict = new Map(db)
    
    if (dict.has(id_pw[0])) {
        return dict.get(id_pw[0]) == id_pw[1] ? "login" : "wrong pw"
    } else {
        return "fail"
    }
}