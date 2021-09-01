import heapq
import sys

hq = []
while True:
    num = int(sys.stdin.readline())
    if num == -1:
        break
    elif num == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(-1)
    else:
        heapq.heappush(hq, num)
