import sys

N = int(sys.stdin.readline())
ppl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ppl.sort(reverse=True)
ans = 0
heavy = 0
for h, w in ppl:
    if w > heavy:
        ans += 1
        heavy = w
print(ans)
