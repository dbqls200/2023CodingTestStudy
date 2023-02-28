# 120883 로그인 성공?

def solution(id_pw, db):
    db = dict(db)
    id, pw = id_pw
    if id in db.keys():
        if pw == db[id]:
            return 'login'
        else:
            return 'wrong pw'
    return 'fail'
