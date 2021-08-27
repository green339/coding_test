import sys

N = int(sys.stdin.readline())
score = map(int, sys.stdin.readline().split())
ans = 0
flag = 1
for s in score:
    if s:
        ans += flag
        flag += 1
    else:
        flag = 1
print(ans)
