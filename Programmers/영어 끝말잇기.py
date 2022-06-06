# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    last = ''
    answer = [0, 0]
    done = []
    for i, w in enumerate(words):
        if i == 0:
            last = w
            done.append(w)
            continue
        if last[-1] != w[0] or w in done:
            answer = [i % n + 1, i // n + 1]
            break
        last = w
        done.append(w)
    return answer


def solution_v2(n, words):
    for i in range(1, len(words)):
        for j in range(i):
            if words[i] == words[j]:
                break
        else:
            if words[i - 1][-1] == words[i][0]:
                continue
        return [i % n + 1, i // n + 1]
    return [0, 0]
