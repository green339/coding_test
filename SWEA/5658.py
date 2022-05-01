# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = deque(list(input()))
    r = N // 4
    numbers = set()
    for _ in range(r):
        for i in range(0, N, r):
            temp = ''
            for j in range(i, i + r):
                temp += arr[j]
            numbers.add(int(temp, 16))
        arr.rotate(1)
    ans = sorted(numbers, reverse=True)[K - 1]
    print(f'#{tc} {ans}')
