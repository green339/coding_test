import sys
from collections import deque

input = sys.stdin.readline


def swap(a, b, d):
    i = d // (10 ** a) % 10
    j = d // (10 ** b) % 10
    d -= i * 10 ** a
    d -= j * 10 ** b
    d += i * 10 ** b
    d += j * 10 ** a
    return d


N, K = map(int, input().split())
m = len(str(N))

nums = set(list(str(N)))
flag=0 # 같은 숫자가 있는지 -> 있으면 11 22 이러면 어떤 바꿔도 같아지니까
if len(nums)!=m:
    flag=1
if m == 1:# 못하는 경우 123456789
    answer = -1
elif m == 2 and '0' in nums: #못하는 경우 10,20 .. 90
    answer = -1
else:
    visited = set()
    q = deque([(N, 0)])
    answer = 0
    while q:
        x, cnt = q.popleft()
        if answer<x: #answer값을 저장할때
            if flag:#같은 수가 두개이상있으면 연산을할때 같은수끼리 움직이면서 채울수 있으니까 언제든 마지막에 이 수를 만들수 있다
                answer=x
            else:
                if (K - cnt) % 2 == 0 and answer < x: # 같은수가 없으면 남은 횟수가 짝수여야 마지막에 다시 그 수를 만들 수 있다
                    answer = x
        if cnt == K:
            continue
        for i in range(m):
            for j in range(i + 1, m):
                nx = swap(i, j, x)
                if nx not in visited:
                    q.append((nx, cnt + 1))
                    visited.add(nx)
print(answer)