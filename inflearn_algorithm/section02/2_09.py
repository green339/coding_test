import sys

N = int(sys.stdin.readline())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
for c in case:
    if len(set(c)) == 3:
        money = max(c) * 6
    elif len(set(c)) == 2:
        c.remove(c[0] ^ c[1] ^ c[2])
        money = c[0] * 100 + 1000
    else:
        money = c[0] * 1000 + 10000
    ans = max(ans, money)
print(ans)