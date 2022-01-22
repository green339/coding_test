# https://www.acmicpc.net/problem/2166
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    loc = [list(map(int, input().split())) for _ in range(N)]
    loc.append(loc[0])
    x = 0
    y = 0
    for i in range(N):
        x += loc[i][0] * loc[i + 1][1]
        y += loc[i][1] * loc[i + 1][0]
    print(round(abs(x - y) * 0.5, 1))

"""
hint 
사선공식을 이용하여 문제를 풀 수 있다.
https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
"""

