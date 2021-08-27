import sys

N = int(sys.stdin.readline())
math = list(map(int, sys.stdin.readline().split()))
avg = round(sum(math) / N)
minus = 100
ans = 0
score = -1
for i, s in enumerate(math):
    tmp = abs(avg - s)
    if tmp < minus or (tmp == minus and s > score):
        score = s
        ans = i + 1
        minus = tmp

print(avg, ans)
