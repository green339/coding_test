# https://www.acmicpc.net/problem/13458
import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    answer=0
    for students in A:
        if students-B<=0:
            answer+=1
        else:
            answer+=1+math.ceil((students-B)/C)
    print(answer)
