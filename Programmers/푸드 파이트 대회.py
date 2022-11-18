# https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    tmp=''
    for idx,f in enumerate(food):
        tmp+=str(idx)*(f//2)
    return tmp+'0'+tmp[::-1]