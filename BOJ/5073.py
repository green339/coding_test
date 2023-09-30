# https://www.acmicpc.net/problem/5073
import sys
input=sys.stdin.readline

tri={1:"Equilateral",2:"Isosceles",3:"Scalene"}
while True:
    board=list(map(int,input().split()))
    if not sum(board):
        break
    board.sort()
    if board[0]+board[1]<=board[2]:
        print("Invalid")
    else:
        print(tri[len(set(board))])
