def solution(n, k, cmd):
    delete = []  # 삭제된 값들 저장 스택
    link = dict()  # linked list
    for x in range(n):
        link[x] = [x - 1, x + 1]  # 맨 끝 값인 경우 -1,8
    for c in cmd:
        c = c.split(" ")
        if c[0] == "D":  # 아래
            for _ in range(int(c[1])):
                k = link[k][1]
        elif c[0] == "U":  # 위
            for _ in range(int(c[1])):
                k = link[k][0]
        elif c[0] == "C":  # 삭제
            s, e = link[k]
            delete.append((k, s, e))
            if e == n:  # 삭제된 행이 가장 마지막 행인 경우
                k = s
            else:
                link[e][0] = s
                k = e
            if s != -1:  # 삭제된 행이 가장 처음 행이 아닌 경우
                link[s][1] = e
        elif c[0] == "Z":  # 복원
            idx, i, j = delete.pop()
            if j != n:  # 복원하는 행이 가장 마지막 행이 아닌 경우
                link[j][0] = idx
            if i != -1:  # 복원하는 행이 가장 처음 행이 아닌 경우
                link[i][1] = idx

    answer = ['O'] * n
    for idx, _, _ in delete:
        answer[idx] = 'X'
    answer = ''.join(answer)
    return answer


def solution_v2(n, k, cmd):
    link = dict()
    delete = []
    cur = k
    for i in range(n):
        link[i] = [i - 1, i + 1]
    for c in cmd:
        c = c.split()
        if c[0] == "U":
            for _ in range(int(c[1])):
                cur = link[cur][0]
        elif c[0] == "D":
            for _ in range(int(c[1])):
                cur = link[cur][1]
        elif c[0] == "C":
            delete.append(cur)
            if link[cur][0] != -1:  # 삭제하는 행이 맨 위 행이 아닌 경우
                link[link[cur][0]][1] = link[cur][1]
            if link[cur][1] == n:  # 삭제하는 행이 가장 마지막 행인 경우
                cur = link[cur][0]
            else:
                link[link[cur][1]][0] = link[cur][0]
                cur = link[cur][1]
        elif c[0] == "Z":
            idx = delete.pop()
            if link[idx][1] != n:
                link[link[idx][1]][0] = idx
            if link[idx][0] != -1:
                link[link[idx][0]][1] = idx
    answer = ['O'] * n
    for d in delete:
        answer[d] = 'X'

    return ''.join(answer)
