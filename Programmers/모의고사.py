def solution(answers):
    ppl = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    cnt = {1: 0, 2: 0, 3: 0}
    for i, a in enumerate(answers):
        for k in range(1, 4):
            cnt[k] += ppl[k][i % len(ppl[k])] == a
    score = max(cnt.values())
    answer = []
    for x, y in cnt.items():
        if y == score:
            answer.append(x)
    return answer
