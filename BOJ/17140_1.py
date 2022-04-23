# https://www.acmicpc.net/problem/17140
from collections import Counter


def sorting(arr):
    sorted_arr = [[] for _ in range(len(arr))]
    temp = []
    max_line = 0
    for ar in arr:
        cnt = Counter(ar)
        if 0 in cnt.keys():
            cnt.pop(0)
        max_line = max(max_line, len(cnt) * 2)
        temp.append(cnt)
    max_line = 100 if max_line > 100 else max_line
    for i in range(len(arr)):
        for kv in sorted(temp[i].items(), key=lambda x: (x[1], x[0])):
            sorted_arr[i].extend(kv)
            if len(sorted_arr[i]) == 100:
                break
        else:
            if len(sorted_arr[i]) < max_line:
                sorted_arr[i].extend([0] * (max_line - len(sorted_arr[i])))
    return sorted_arr


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
for t in range(102):
    if len(A) >= r and len(A[0]) >= c and A[r - 1][c - 1] == k:
        break
    if len(A) >= len(A[0]):
        A = sorting(A)
    else:
        A = list(zip(*sorting(list(zip(*A)))))
print(t if t <= 100 else -1)
