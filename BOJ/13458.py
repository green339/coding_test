# https://www.acmicpc.net/problem/13458
import sys
import math

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    answer = 0
    for ppl in A:
        answer += 1
        ppl -= B
        if ppl > 0:
            answer += math.ceil(ppl / C)
    print(answer)
