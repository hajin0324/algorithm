def solution(id_pw, db):
    db = {d[0] : d[1] for d in db}
    
    if id_pw[0] in db:
        if id_pw[1] == db[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"