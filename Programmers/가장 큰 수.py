# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    answer = ''
    if max(numbers) == 0:
        return "0"
    sn = [(str(i), (str(i) * 4)[:4]) for i in numbers]

    sn.sort(key=lambda x: x[1], reverse=True)
    answer = ''.join([answer + i[0] for i in sn])
    return answer


def solution_v2(numbers):
    if max(numbers) == 0:
        return "0"
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return ''.join(numbers)
