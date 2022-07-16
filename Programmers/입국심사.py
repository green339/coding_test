# https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0
    times.sort()
    start = times[0]
    end = times[-1] * n
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n:
                answer = mid
                end = mid - 1
                break
        else:
            start = mid + 1
    return answer


def solution(n, times):
    times.sort()
    start = times[0]
    end = times[-1] * n
    while start < end:
        mid = (start + end) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
        if cnt >= n:
            end = mid
        else:
            start = mid + 1
    return start
