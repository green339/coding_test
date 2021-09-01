import sys

arr, m = map(int, sys.stdin.readline().split())
arr = list(map(int, str(arr)))
stack = []
for a in arr:
    while stack and stack[-1] < a and m > 0:
        stack.pop()
        m -= 1
    stack.append(a)
while m:
    stack.pop()
    m -= 1
for s in stack:
    print(s, end='')
