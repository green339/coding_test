# https://www.acmicpc.net/problem/2606
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    computer = defaultdict(list)
    ans = set()
    ans.add(1)
    _ = int(input())
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        computer[a].append(b)
        computer[b].append(a)
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        for nx in computer[x]:
            if nx not in ans:
                ans.add(nx)
                q.append(nx)
    print(len(ans) - 1)
