import sys
input=sys.stdin.readline

board = [[0] * 101 for _ in range(101)]
direction=[(1,0),(0,-1),(-1,0),(0,1)]
N=int(input())

for _ in range(N):
    x,y,d,g=map(int,input().split())
    board[x][y] = 1
    curve = [d]
    x += direction[d][0]
    y += direction[d][1]
    board[x][y] = 1
    for i in range(1, g + 1):
        for j in range(2 ** (i - 1) - 1, -1, -1):
            d = (curve[j] + 1) % 4
            x += direction[d][0]
            y += direction[d][1]
            board[x][y] = 1
            curve.append(d)
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
            answer += 1
print(answer)