# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for one, two in zip(arr1[i], arr2[i]):
            temp.append(one + two)
        answer.append(temp)
    return answer


### 오오오!!
def solution(arr1, arr2):
    answer = [list(map(sum, zip(*arr))) for arr in zip(arr1, arr2)]
    return answer
