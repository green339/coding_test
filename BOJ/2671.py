# https://www.acmicpc.net/problem/2671
import sys
import re

input = sys.stdin.readline
if __name__ == "__main__":
    sign = input().strip()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(sign):
        print("SUBMARINE")
    else:
        print("NOISE")
