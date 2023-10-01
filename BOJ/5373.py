# https://www.acmicpc.net/problem/5373
import sys
input=sys.stdin.readline


def U(flag):
    if flag == '-':
        cube[0] = list(map(list,zip(*cube[0])))[::-1]
        cube[3] = list(map(list,zip(*cube[3])))[::-1]
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        tmp = cube[1][0]
        cube[1][0] = cube[4][0]
        cube[4][0] = tmp
        tmp = cube[5][0]
        cube[5][0] = cube[4][0]
        cube[4][0] = tmp
        tmp = cube[3][0]
        cube[3][0] = cube[4][0]
        cube[4][0] = tmp
        cube[3] = list(map(list, zip(*cube[3][::-1])))
        cube[3] = list(map(list, zip(*cube[3][::-1])))
    else:
        cube[0]=list(map(list,zip(*cube[0][::-1])))
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        tmp=cube[3][0]
        cube[3][0]=cube[4][0]
        cube[4][0]=tmp
        tmp=cube[5][0]
        cube[5][0]=cube[4][0]
        cube[4][0]=tmp
        tmp = cube[1][0]
        cube[1][0] = cube[4][0]
        cube[4][0] = tmp
        cube[3] = list(map(list, zip(*cube[3][::-1])))
        cube[3] = list(map(list, zip(*cube[3][::-1])))

def D(flag):
    if flag == '+':
        cube[2] = list(map(list,zip(*cube[2][::-1])))
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        tmp = cube[1][2]
        cube[1][2] = cube[4][2]
        cube[4][2] = tmp
        tmp = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = tmp
        tmp = cube[3][2]
        cube[3][2] = cube[4][2]
        cube[4][2] = tmp
        cube[3] = list(map(list, zip(*cube[3][::-1])))
        cube[3] = list(map(list, zip(*cube[3][::-1])))
    else:
        cube[2]=list(map(list,zip(*cube[2])))[::-1]
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        cube[3] = list(map(list, zip(*cube[3])))[::-1]
        tmp=cube[3][2]
        cube[3][2]=cube[4][2]
        cube[4][2]=tmp
        tmp=cube[5][2]
        cube[5][2]=cube[4][2]
        cube[4][2]=tmp
        tmp = cube[1][2]
        cube[1][2] = cube[4][2]
        cube[4][2] = tmp
        cube[3] = list(map(list, zip(*cube[3][::-1])))
        cube[3] = list(map(list, zip(*cube[3][::-1])))

def F(flag):
    if flag == '+':
        cube[1] = list(map(list,zip(*cube[1][::-1])))
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[4] = list(map(list,zip(*cube[4][::-1])))
        cube[5] = list(map(list,zip(*cube[5])))[::-1]
        tmp = cube[0][2]
        cube[0][2] = cube[4][2]
        cube[4][2] = tmp
        tmp = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = tmp
        tmp = cube[2][2]
        cube[2][2] = cube[4][2]
        cube[4][2] = tmp
        cube[4] = list(map(list,zip(*cube[4])))[::-1]
        cube[5] = list(map(list,zip(*cube[5][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))
    else:
        cube[1] = list(map(list,zip(*cube[1])))[::-1]
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[4] = list(map(list,zip(*cube[4][::-1])))
        cube[5] = list(map(list,zip(*cube[5])))[::-1]
        tmp = cube[2][2]
        cube[2][2] = cube[4][2]
        cube[4][2] = tmp
        tmp = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = tmp
        tmp = cube[0][2]
        cube[0][2] = cube[4][2]
        cube[4][2] = tmp
        cube[4] = list(map(list,zip(*cube[4])))[::-1]
        cube[5] = list(map(list,zip(*cube[5][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))

def B(flag):
    if flag == '-':
        cube[3] = list(map(list,zip(*cube[3])))[::-1]
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[4] = list(map(list,zip(*cube[4][::-1])))
        cube[5] = list(map(list,zip(*cube[5])))[::-1]
        tmp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = tmp
        tmp = cube[5][0]
        cube[5][0] = cube[4][0]
        cube[4][0] = tmp
        tmp = cube[2][0]
        cube[2][0] = cube[4][0]
        cube[4][0] = tmp
        cube[4] = list(map(list,zip(*cube[4])))[::-1]
        cube[5] = list(map(list,zip(*cube[5][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))
    else:
        cube[3] = list(map(list,zip(*cube[3][::-1])))
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[2] = list(map(list, zip(*cube[2])))[::-1]
        cube[4] = list(map(list,zip(*cube[4][::-1])))
        cube[5] = list(map(list,zip(*cube[5])))[::-1]
        tmp = cube[2][0]
        cube[2][0] = cube[4][0]
        cube[4][0] = tmp
        tmp = cube[5][0]
        cube[5][0] = cube[4][0]
        cube[4][0] = tmp
        tmp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = tmp
        cube[4] = list(map(list,zip(*cube[4])))[::-1]
        cube[5] = list(map(list,zip(*cube[5][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))
        cube[2] = list(map(list, zip(*cube[2][::-1])))

def L(flag):
    if flag == '+':
        cube[4] = list(map(list,zip(*cube[4][::-1])))
        for i in range(1,4):
            for j in range(3):
                tmp=cube[i][j][0]
                cube[i][j][0]=cube[0][j][0]
                cube[0][j][0]=tmp
    else:
        cube[4] = list(map(list,zip(*cube[4])))[::-1]
        for i in range(3, 0,-1):
            for j in range(3):
                tmp = cube[i][j][0]
                cube[i][j][0] = cube[0][j][0]
                cube[0][j][0] = tmp

def R(flag):
    if flag == '-':
        cube[5] = list(map(list,zip(*cube[5])))[::-1]
        for i in range(1,4):
            for j in range(3):
                tmp=cube[i][j][2]
                cube[i][j][2]=cube[0][j][2]
                cube[0][j][2]=tmp
    else:
        cube[5] = list(map(list,zip(*cube[5][::-1])))
        for i in range(3, 0,-1):
            for j in range(3):
                tmp = cube[i][j][2]
                cube[i][j][2] = cube[0][j][2]
                cube[0][j][2] = tmp

T=int(input())
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
        if c[0]=="U":
            U(c[1])
        elif c[0]=="D":
            D(c[1])
        elif c[0]=="F":
            F(c[1])
        elif c[0]=="B":
            B(c[1])
        elif c[0]=="L":
            L(c[1])
        elif c[0]=="R":
            R(c[1])
    for b in cube[0]:
        print(''.join(b))