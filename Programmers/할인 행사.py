# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0
    total=[]
    for i in range(len(want)):
        for _ in range(number[i]):
            total.append(want[i])
    total.sort()
    for i in range(len(discount)-9):
        tmp= discount[i:i+10]
        if set(tmp)==set(want) and total==sorted(tmp):
            answer+=1
    return answer