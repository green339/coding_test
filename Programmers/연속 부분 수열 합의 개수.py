# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    sums=set()
    for l in range(len(elements)):
        tmp=elements+elements[:l]
        for i in range(len(tmp)-l):
            sums.add(sum(tmp[i:i+l+1]))
    return len(sums)