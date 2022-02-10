# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for n in numbers:
        if n % 4 == 3:
            idx = 2
            while True:
                if not n & (2 ** idx):
                    answer.append(n + 2 ** (idx - 1))
                    break
                idx += 1
        else:
            answer.append(n + 1)
    return answer
