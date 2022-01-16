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
