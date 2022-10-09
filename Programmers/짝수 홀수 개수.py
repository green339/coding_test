# https://school.programmers.co.kr/learn/courses/30/lessons/120824
def solution(num_list):
    res = [i%2 for i in num_list]
    return [res.count(0),res.count(1)]