# https://www.acmicpc.net/problem/9207
import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(pins, holes, cnt):
    n = 0
    while n < len(pins):
        x = pins[n][0]
        y = pins[n][1]
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in pins:
                nnx = nx + dx
                nny = ny + dy
                if (nnx, nny) in holes:
                    # 지문대로 실행
                    pins.remove((x, y))
                    temp = pins.index((nx, ny))
                    pins.remove((nx, ny))
                    holes.add((x, y))
                    holes.add((nx, ny))
                    holes.remove((nnx, nny))
                    pins.append((nnx, nny))

                    dfs(pins, holes, cnt + 1)

                    # (백트래킹)원래대로 -> 이때 같은 위치로 넣어야함 (인덱스이용)
                    count.append((len(pins), cnt + 1))  # 더이상 움직일 수 없는 경우 백트래킹 -> 그 때의 이동 핀 수를 체크해둠
                    pins.insert(temp, (nx, ny))
                    pins.insert(n, (x, y))
                    holes.remove((x, y))
                    holes.remove((nx, ny))
                    holes.add((nnx, nny))
                    pins.remove((nnx, nny))
        n += 1


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for _ in range(N):
        count = []
        pin = []
        hole = set()
        for x in range(5):
            row = list(sys.stdin.readline().strip())
            for y, b in enumerate(row):
                if b == 'o':
                    pin.append((x, y))
                elif b == '.':
                    hole.add((x, y))
        _ = sys.stdin.readline()
        dfs(pin, hole, 0)
        if count:
            print(*sorted(count)[0])
        else:
            print("%d 0" % len(pin))
