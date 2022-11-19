# https://school.programmers.co.kr/learn/courses/30/lessons/131704
def solution(order):
    answer = 0
    stack=[]
    for i in range(len(order)):
        stack.append(i+1)
        while stack and order[answer]==stack[-1]:
            answer+=1
            stack.pop()
    return answer