import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
left = 0
right = N - 1
ans = []
last = 0
while left <= right:
    l = arr[left]
    r = arr[right]
    if l > r > last or l < last < r:
        ans.append("R")
        last = r
        right -= 1
    elif r > l > last or r < last < l:
        ans.append("L")
        last = l
        left += 1
    else:
        break
    if left == right:
        ans.pop()
        ans.append("L")

print(''.join(ans))
