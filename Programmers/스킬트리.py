# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        skills = [s for s in st if s in skill]
        for a, b in zip(skills, skill):
            if a != b:
                break
        else:
            answer += 1
    return answer
