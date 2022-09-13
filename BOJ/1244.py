# https://www.acmicpc.net/problem/1244
import sys

input = sys.stdin.readline

change = {1: 0, 0: 1}
n = int(input())
switch = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num - 1, n, num):
            switch[i] = change[switch[i]]
    else:
        switch[num - 1] = change[switch[num - 1]]
        for d in range(1, min(n - num + 1, num)):
            left = num - 1 - d
            right = num - 1 + d
            if switch[left] == switch[right]:
                switch[left] = change[switch[left]]
                switch[right] = change[switch[right]]
            else:
                break
for s in range(0, n, 20):
    print(*switch[s:s + 20])
