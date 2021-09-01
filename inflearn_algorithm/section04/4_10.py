import sys

N = int(sys.stdin.readline())
inverse = list(map(int, sys.stdin.readline().split()))
ans = [N]
for i in range(N - 1, 0, -1):
    ans.insert(inverse[i - 1], i)
print(*ans)
