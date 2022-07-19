# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    global answer
    answer = 1e9

    def dfs(move, i):
        global answer
        if move >= answer:
            return
        if not sum(arr):
            answer = min(move, answer)
            return
        for d in [-1, 1]:
            for cnt in range(n):
                ni = (i + d * cnt) % n
                if arr[ni]:
                    break
            tmp = arr[ni]
            arr[ni] = 0
            dfs(move + cnt + tmp, ni)
            arr[ni] = tmp

    n = len(name)
    arr = [min(ord(m) - ord('A'), ord('Z') + 1 - ord(m)) for m in name]
    start = arr[0]
    arr[0] = 0
    dfs(start, 0)
    return answer
