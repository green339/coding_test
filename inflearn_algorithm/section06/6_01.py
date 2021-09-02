import sys


def binary(k):
    if k > 1:
        binary(k // 2)
    print(k % 2, end='')


N = int(sys.stdin.readline())
binary(N)
