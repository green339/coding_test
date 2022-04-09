# https://programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 1  # 자기자신 포함
    # 슬라이딩 윈도우
    numbers = [i for i in range(1, n // 2 + 2)]
    if n < 3:
        return answer
    l, r = 0, 0
    tmp = 0
    while r <= len(numbers):
        if tmp >= n:
            if tmp == n:
                answer += 1
            tmp -= numbers[l]
            l += 1
        else:
            if r < len(numbers):
                tmp += numbers[r]
            r += 1
    return answer
