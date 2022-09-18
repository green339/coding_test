# https://www.acmicpc.net/problem/1003
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        zero = [1, 0]
        one = [0, 1]
        for x in range(2, N + 1):
            zero.append(zero[-1] + zero[-2])
            one.append(one[-1] + one[-2])
        print(zero[N], one[N])
