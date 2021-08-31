import sys

n = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
ans = 0
end = 0
for s, e in meetings:
    if s >= end:
        ans += 1
        end = e
print(ans)
