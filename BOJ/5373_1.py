# https://www.acmicpc.net/problem/5373
import sys
input=sys.stdin.readline

def move(surround,flag,cur,d):
    if d==1: #시계
        cube[cur] = list(map(list,zip(*cube[cur][::-1])))
    else: #반시계
        cube[cur] = list(map(list, zip(*cube[cur])))[::-1]
    for i in range(1, 4):
        for j in range(3):
            tmp = cube[surround[i]][flag][j]
            cube[surround[i]][flag][j] = cube[surround[0]][flag][j]
            cube[surround[0]][flag][j] = tmp

T=int(input())
parameter={"U+":[[4,3,5,1],0,0,1], "U-":[[4,1,5,3],0,0,-1],
           "D+":[[4,1,5,3],2,2,1], "D-":[[4,3,5,1],2,2,-1],
           "F+":[[4,0,5,2],2,1,1], "F-":[[4,2,5,0],2,1,-1],
           "B+":[[4,2,5,0],0,3,1], "B-":[[4,0,5,2],0,3,-1],
           "L+":[[0,1,2,3],0,4,1], "L-":[[0,3,2,1],0,4,-1],
           "R+":[[0,3,2,1],2,5,1], "R-":[[0,1,2,3],2,5,-1]}
for _ in range(T):
    n=int(input())
    cmd=list(input().split())
    cube = [[["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],
            [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],
            [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],
            [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]],
            [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],
            [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]]]
    for c in cmd:
        if c[0]=="U" or c[0]=="D":
            cube[3] = list(map(list,map(reversed,cube[3][::-1])))
            move(*parameter[c])
            cube[3] = list(map(list, map(reversed, cube[3][::-1])))
        elif c[0]=="F" or c[0]=="B":
            cube[2] = list(map(list,map(reversed,cube[2][::-1])))
            cube[4] = list(map(list, zip(*cube[4][::-1])))
            cube[5] = list(map(list, zip(*cube[5])))[::-1]
            move(*parameter[c])
            cube[2] = list(map(list,map(reversed,cube[2][::-1])))
            cube[4] = list(map(list, zip(*cube[4])))[::-1]
            cube[5] = list(map(list, zip(*cube[5][::-1])))
        elif c[0]=="L" or c[0]=="R":
            for r in range(4):
                cube[r] = list(map(list, zip(*cube[r][::-1])))
            move(*parameter[c])
            for r in range(4):
                cube[r] = list(map(list, zip(*cube[r])))[::-1]
    for b in cube[0]:
        print(''.join(b))