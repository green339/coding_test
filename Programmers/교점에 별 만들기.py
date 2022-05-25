# https://programmers.co.kr/learn/courses/30/lessons/87377
def solution(line):
    INF = float('inf')
    star = set()
    min_x = INF
    min_y = INF
    max_x = -INF
    max_y = -INF
    end = len(line)
    for i in range(end):
        a, b, e = line[i]
        for j in range(i + 1, end):
            c, d, f = line[j]
            tmp = (a * d - b * c)
            if not tmp:
                continue
            x = (b * f - e * d) / tmp
            if not x.is_integer():
                continue
            y = (e * c - a * f) / tmp
            if not y.is_integer():
                continue
            star.add((x, y))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
    answer = [["."] * (int(max_y - min_y) + 1) for _ in range(0, int(max_x - min_x) + 1)]
    for i, j in star:
        answer[int(i - min_x)][int(j - min_y)] = "*"

    return [''.join(a) for a in zip(*answer)][::-1]
