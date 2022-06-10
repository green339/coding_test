# https://programmers.co.kr/learn/courses/30/lessons/12936

def solution(n, k):
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i
    numbers = [i for i in range(1, n + 1)]
    answer = []
    for i in range(n - 1, 0, -1):
        q, k = divmod(k, factorial[i])
        if k == 0:
            q -= 1
        answer.append(numbers[q])
        numbers.remove(numbers[q])
        if k == 0:
            answer.extend(numbers[::-1])
            break
    return answer
