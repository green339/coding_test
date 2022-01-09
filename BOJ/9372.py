# https://www.acmicpc.net/problem/9372
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        for _ in range(M):
            _, _ = map(int, input().split())
        print(N - 1)  # 최소 신장 트리 N개의 정점(국가)-> 간선의 수: N-1
