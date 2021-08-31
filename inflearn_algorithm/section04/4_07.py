import sys

L = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr.sort()
for _ in range(M):
    arr[0]+=1
    arr[-1]-=1
    arr.sort()

print(arr[-1]-arr[0])
