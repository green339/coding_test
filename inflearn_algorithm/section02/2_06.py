import sys


def digit_sum(x):
    l = len(str(x))
    a = 0
    for t in range(l, -1, -1):
        a += x // 10 ** t
        x %= 10 ** t
    # a = sum(list(map(int, str(x))))
    return a


N = int(sys.stdin.readline())
ans = 0
total = 0
for i in map(int, sys.stdin.readline().split()):
    tmp = digit_sum(i)
    if total < tmp:
        ans = i
        total = tmp
print(ans)
