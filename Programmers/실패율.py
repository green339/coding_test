def solution(N, stages):
    answer = dict()
    stage = [0] * (N + 2)  # 도달한 유저수
    for usr in stages:
        for i in range(1, usr + 1):
            stage[i] += 1
    for idx in range(1, N + 1):
        if stage[idx]:
            answer[idx] = (stage[idx] - stage[idx + 1]) / stage[idx]
        else:
            answer[idx] = 0
    return sorted(answer, key=lambda x: answer[x], reverse=True)
