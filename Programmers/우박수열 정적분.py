# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    dp=[0]
    prior=k
    while k>1:
        if k%2:
            k=k*3+1
        else:
            k//=2
        dp.append((prior+k)/2+dp[-1])
        prior=k
    end=len(dp)-1
    for a,b in ranges:
        b=end+b
        if a>b:
            answer.append(-1)
        else:
            answer.append(dp[b]-dp[a])
    return answer