import sys
from collections import deque

order = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
for i in range(1, N + 1):
    plan = sys.stdin.readline().strip()
    q = deque(order)
    flag = 1
    for p in plan:
        if p in q:
            if q.popleft() != p:
                flag = 0
                break
    if flag: # 이거 대신에 for ~ else문을 써서 할 수 있음
        if q:
            print(f'#{i} NO')
        else:
            print(f'#{i} YES')
    else:
        print(f'#{i} NO')

