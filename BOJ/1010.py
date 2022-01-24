# https://www.acmicpc.net/problem/1010
import sys

input = sys.stdin.readline


def factorial(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(factorial(M) // (factorial(N) * factorial(M - N)))
