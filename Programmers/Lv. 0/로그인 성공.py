def solution(id_pw, db):
    # id_pw: [id, pw]
    # db: [[id1, pw1], [id2, pw2], [id3, pw3]]
    
    dict_db = {id:pw for id, pw in db}
    
    for id, pw in dict_db.items():
        if id_pw[0] == id:
            if id_pw[1] == pw:
                return 'login'
            else:
                return 'wrong pw'
        
    return 'fail'
