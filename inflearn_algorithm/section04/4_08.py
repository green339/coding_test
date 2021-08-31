import sys

N, M = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
w.sort()
left = 0
right = N - 1
ans = 0
while left <= right:
    if w[left] + w[right] <= M:
        left += 1
        right -= 1
        ans += 1
    else:
        right -= 1
        ans += 1
print(ans)
