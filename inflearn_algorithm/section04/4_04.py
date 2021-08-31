import sys

N, C = map(int, sys.stdin.readline().split())
board = [int(sys.stdin.readline()) for _ in range(N)]
board.sort()

left = 1
right = board[-1] - board[0]
ans = 0
while left <= right:
    mid = (left + right) // 2
    pos = -10 ** 9
    cnt = 0
    for b in board:
        if b - pos >= mid:
            cnt += 1
            pos = b
    if cnt >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
