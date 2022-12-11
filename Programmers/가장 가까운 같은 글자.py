# https://school.programmers.co.kr/learn/courses/30/lessons/142086

from collections import defaultdict
def solution(s):
    answer = []
    alphas=defaultdict(int)
    for idx in range(len(s)):
        if alphas[s[idx]]:
            answer.append(idx+1-alphas[s[idx]])
        else:
            answer.append(-1)
        alphas[s[idx]]=idx+1
    return answer