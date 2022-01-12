# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    answer = ''
    if max(numbers) == 0:
        return "0"
    sn = [(str(i), (str(i) * 4)[:4]) for i in numbers]

    sn.sort(key=lambda x: x[1], reverse=True)
    print(sn)
    answer = ''.join([answer + i[0] for i in sn])
    return answer
