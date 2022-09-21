import copy


def solution(n, info):
    global diff, answer

    def dfs(cur, idx):
        global diff, answer
        if cur == 0:
            apeach = 0
            ryan = 0
            for k in range(10):
                if not info[k] and not cand[k]:
                    continue
                if info[k] >= cand[k]:
                    apeach += (10 - k)
                else:
                    ryan += (10 - k)
            if ryan - apeach > diff:
                answer = copy.deepcopy(cand)
                diff = ryan - apeach
            return
        if idx < 0:
            return
        for i in range(cur, -1, -1):
            cand[idx] = i
            dfs(cur - i, idx - 1)

    diff = 0
    cand = [0] * 11
    answer = [0] * 11
    dfs(n, 10)
    return answer
