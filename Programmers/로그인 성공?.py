# https://school.programmers.co.kr/learn/courses/30/lessons/120883
def solution(id_pw, db):
    member = dict(db)
    if id_pw[0] not in member.keys():
        return "fail"
    elif member[id_pw[0]] != id_pw[1]:
        return "wrong pw"
    return "login"
