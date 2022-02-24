# https://www.acmicpc.net/problem/1655
import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lq = []
    rq = []
    for _ in range(n):
        x = int(input())
        if len(lq) <= len(rq):
            heapq.heappush(lq, -x)
        else:
            heapq.heappush(rq, x)
        if rq and -lq[0] > rq[0]:
            heapq.heappush(rq, -heapq.heappop(lq))
            heapq.heappush(lq, -heapq.heappop(rq))
        print(-lq[0])
