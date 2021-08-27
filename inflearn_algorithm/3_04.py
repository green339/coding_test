import sys

N = int(sys.stdin.readline())
one = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
two = list(map(int, sys.stdin.readline().split()))
ans = []
l1, l2 = one.pop(0), two.pop(0)
while one or two:
    if l1 <= l2:
        ans.append(l1)
        l1 = one.pop(0) if one else sys.maxsize

    else:
        ans.append(l2)
        l2 = two.pop(0) if two else sys.maxsize
ans.append(l2 if l2 != sys.maxsize else l1)
print(*ans)
