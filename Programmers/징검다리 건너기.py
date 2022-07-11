# https://school.programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    rocks = sorted(stones)
    start = rocks[0]
    end = rocks[-1]
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for s in stones:
            if s > mid:
                cnt = 0
            else:
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
        else:
            start = mid + 1
    return start
