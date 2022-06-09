# https://programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = []
    for a in arr1:
        row = []
        for b in zip(*arr2):
            row.append(sum([i * j for i, j in zip(a, b)]))
        answer.append(row)
    return answer
