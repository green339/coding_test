# https://www.acmicpc.net/problem/17825
import sys

input = sys.stdin.readline

route = dict()
route[0] = [i for i in range(0, 41, 2)] + [0]
route[10] = [10, 13, 16, 19, 25, 30, 35, 40, 0]
route[20] = [20, 22, 24, 25, 30, 35, 40, 0]
route[30] = [30, 28, 27, 26, 25, 30, 35, 40, 0]


def dfs(cur, depth):
    def check(k, v, ii):
        if route[k][v] == 0:  # 도착점인 경우
            return True
        for ss in range(4):
            if ss == ii:
                continue
            if dice[ss] == [k, v]:
                return False
            elif route[k][v] == route[dice[ss][0]][dice[ss][1]]:
                if 30 in [k,dice[ss][0]] and route[k][v] == 30:
                    continue
                elif 0 in [k, dice[ss][0]] and route[k][v] in [16, 22, 24, 26, 28]:
                    continue

                return False
        return True

    global answer

    if depth == 10:
        answer = max(answer, cur)
        return
    start = 0
    for i in range(4):  # 어떤 주사위를 선택할지
        dk, dv = dice[i]
        if dk == 0 and dv == 0:
            if start:
                continue
            else:
                start += 1
        if dk == 0 and dv == 0 or route[dk][dv] != 0:  # 도착점이 아닌 경우
            # 루트대로 말을 움직인다.
            ndk = dk
            ndv = min(len(route[dk]) - 1, dv + order[depth])
            if dk == 0 and route[dk][ndv] in [10, 20, 30]:  # 도착지점이 파랑동그라미면
                ndk = route[dk][ndv]
                ndv = 0
            # 만약 거기에 다른 말이 없으면
            if check(ndk, ndv, i):
                dice[i] = [ndk, ndv]
                dfs(cur + route[ndk][ndv], depth + 1)
                dice[i] = [dk, dv]


answer = 0
dice = [[0, 0], [0, 0], [0, 0], [0, 0]]  # route의 키, idx / -1이면 도착점에 도착한 말
sx = 0
order = list(map(int, input().split()))
dfs(0, 0)
print(answer)
