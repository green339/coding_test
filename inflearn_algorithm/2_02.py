import sys

T = int(sys.stdin.readline())
case = dict()
for i in range(1, T + 1):
    N, s, e, k = map(int, sys.stdin.readline().split())
    integers = list(map(int, sys.stdin.readline().split()))
    # temp = sorted(integers[s - 1:e])
    temp = sorted([integers[k] for k in range(s - 1, e)])
    case[i] = temp[k - 1]
for key, value in case.items():
    print(f"#{key} {value}")
