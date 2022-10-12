# https://school.programmers.co.kr/learn/courses/30/lessons/120869
def solution(spell, dic):
    spell = set(spell)
    for d in dic:
        if spell == set(d) and len(spell) == len(d):
            return 1
    return 2
